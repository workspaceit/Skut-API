from rest_framework import serializers
from stands.models import Stand
from areas.serializer import AreaSerializer


class StandSerializer(serializers.ModelSerializer):
    area = AreaSerializer(read_only=True)
    area_id = serializers.CharField(write_only=True)

    class Meta:
        model = Stand
        fields = ('id', 'name', 'description', 'coordinate', 'area', 'area_id')


