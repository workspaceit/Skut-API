from rest_framework import serializers
from rides.models import Ride
from stands.stand_serializer import StandSerializer
from scooters.scooter_serializer import ScooterSerializer
from users.user_serializer import UserProfileSerializer


class RideSerializer(serializers.ModelSerializer):
    start_stand = StandSerializer(read_only=True)
    start_stand_id = serializers.CharField(write_only=True)
    end_stand = StandSerializer(read_only=True)
    end_stand_id = serializers.CharField(write_only=True, required=False)
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)
    scooter = ScooterSerializer(read_only=True)
    scooter_id = serializers.CharField(write_only=True)

    class Meta:
        model = Ride
        fields = (
            'id', 'status', 'start_time', 'end_time', 'start_location', 'end_location',
            'start_stand', 'end_stand', 'start_stand_id', 'end_stand_id', 'distance', 'charge',
            'user', 'user_id', 'scooter', 'scooter_id', 'created_at'
        )


