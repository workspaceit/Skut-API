from rest_framework import serializers
from notices.models import Notice


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'title', 'message', 'created_at', 'updated_at', 'created_by', 'updated_by')
