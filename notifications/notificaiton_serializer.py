from rest_framework import serializers
from notifications.models import Notification
from users.user_serializer import UserProfileSerializer


class NotificationSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'title', 'message', 'created_at', 'updated_at', 'user_id', 'user')


