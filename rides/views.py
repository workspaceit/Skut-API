from rest_framework import viewsets, status
from rides.models import Ride
from scooters.models import Scooter
from rides.ride_serializer import RideSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime


class RidePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = (RidePermission,)


class RideAPi:
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = (RidePermission,)

    @api_view(["get"])
    def ride_history_by_user(request):
        user_id = "8748ad3cdebf4d27a3cf87ef8de57b01"
        ride_history_by_user = Ride.objects.filter(user=user_id)
        list_data = []
        for ride in ride_history_by_user:
            serializer = RideSerializer(ride)
            list_data.append(serializer.data)
        return Response(data=[], status=status.HTTP_200_OK)

    @api_view(["post"])
    def ride_by_scan(request):
        scan_data = request.data
        scooter_by_key_name = Scooter.objects.filter(key_name=scan_data.get('key_name'))
        scooter = scooter_by_key_name.first().id

        new_ride = Ride(
            start_stand_id="37362163833c4725b4b680a6bc6d7a3b",
            user_id="8748ad3cdebf4d27a3cf87ef8de57b01",
            scooter_id=scooter
        )
        new_ride.save()
        serialized = RideSerializer(new_ride).data

        return Response(data=serialized, status=status.HTTP_201_CREATED)

    @api_view(["post"])
    def stop_ride(request):
        user_id = "8748ad3cdebf4d27a3cf87ef8de57b01"
        current_ride = Ride.objects.filter(user_id=user_id).first()
        current_ride.end_stand_id = request.data.get('end_stand')
        current_ride.end_time = datetime.datetime.now()
        current_ride.status = 'Completed'
        print(current_ride)
        current_ride.save()
        serialized = RideSerializer(current_ride).data

        return Response(data=serialized, status=status.HTTP_201_CREATED)
