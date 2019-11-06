from rest_framework import serializers
from locks.models import Lock


class LockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lock
        fields = ('id', 'name', 'description', 'status', 'created_at')
