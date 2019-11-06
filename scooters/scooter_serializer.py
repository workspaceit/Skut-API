from rest_framework import serializers
from scooters.models import Scooter
from stands.stand_serializer import StandSerializer
from scooter_models.scooter_model_serializer import ScooterModelSerializer
from locks.locks_serializer import LockSerializer


class ScooterSerializer(serializers.ModelSerializer):
    stand = StandSerializer(read_only=True)
    stand_id = serializers.CharField(write_only=True)
    model = ScooterModelSerializer(read_only=True)
    model_id = serializers.CharField(write_only=True)
    lock = LockSerializer(read_only=True)
    lock_id = serializers.CharField(write_only=True)

    class Meta:
        model = Scooter
        fields = ('id', 'key_name',  'description', 'image', 'status', 'model', 'model_id', 'stand', 'stand_id', 'lock', 'lock_id', 'created_at')
