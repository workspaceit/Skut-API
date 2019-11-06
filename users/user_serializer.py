import random, string
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.utils import model_meta
from django.contrib.auth.hashers import make_password
from users.models import UserProfile
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.db import transaction
from twilio.rest import Client


def send_reg_code(registration_code):
    # Your Account SID from twilio.com/console
    account_sid = "AC0079e5fb9e82061f7619fd0236cf531f"
    # Your Auth Token from twilio.com/console
    auth_token = "102c5188bfbd89d60a90bbd61d52e0f6"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+8801924360176",
        from_="+19045523633",
        body=registration_code)


def generate_registration_code():
    # key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    key = '1234'
    return key


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirm_password')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('uid', 'user', 'phone_number', 'dob', 'address')

    def create(self, validated_data):
        user = UserProfile.objects.filter(phone_number=validated_data.get('phone_number'))
        if not user.exists():
            phone_number = validated_data.get('phone_number')
            registration_code = generate_registration_code()
            UserProfile.objects.create(phone_number=phone_number,
                                       registration_code=registration_code)
            send_reg_code(registration_code)
            response = dict(
                status=True, phone_number=phone_number,
                message="Verification code is sent to your phone number")
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = dict(status=True, message="user found")
            return Response(response, status=status.HTTP_200_OK)

    def check_registration_code(self, validated_date):
        response = dict(status=False, message="Wrong code is provided!")
        registration_code = validated_date.get('registration_code')
        phone_number = validated_date.get('phone_number')
        if UserProfile.objects.filter(registration_code=registration_code, phone_number=phone_number).exists():
            response['status'] = True
            response['message'] = "Success"
            return Response(response, status=status.HTTP_200_OK)

        return Response(response, status=status.HTTP_404_NOT_FOUND)

    @transaction.atomic
    def final_create(self, validated_data):
        """final registration and Inserted to User table"""
        user_data = validated_data.get('user', {})
        password = user_data['password']
        confirm_password = user_data.pop('confirm_password', '')
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords did not match"})
        if User.objects.filter(username=validated_data['phone_number']).exists():
            raise serializers.ValidationError({"phone_number": "Phone number already exists!"})

        user_profile = UserProfile.objects.get(phone_number=validated_data['phone_number'], user__isnull=True)
        user_data['password'] = make_password(password=password)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user_profile.user = user
        user_profile.save()
        user_group = Group.objects.get(name='user')
        user_profile.user.groups.add(user_group)
        return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)

    def update(self, instance, validated_data):
        # method: PUT & PATCH both
        # manually update relational user data
        user_data = validated_data.pop('user', {})
        password = user_data.get('password', '')
        if len(password) > 0:
            confirm_password = user_data.pop('confirm_password', '')
            if password != confirm_password:
                raise serializers.ValidationError("Confirm password didn't match.")
            user_data['password'] = make_password(password)
        UserSerializer.update(UserSerializer(), instance.user, user_data)
        # manual update ends

        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance
