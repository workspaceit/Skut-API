from rest_framework import serializers
from transactions.models import Transaction
from users.user_serializer import UserProfileSerializer
from rides.ride_serializer import RideSerializer


class TransactionSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)
    ride = RideSerializer(read_only=True)
    ride_id = serializers.CharField(write_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'status', 'created_at', 'updated_at', 'user', 'user_id', 'ride', 'ride_id')
