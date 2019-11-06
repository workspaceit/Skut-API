from rest_framework import serializers
from settings.models import Setting


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = ('id', 'key', 'value', 'created_at', 'updated_at', 'created_by', 'updated_by')


