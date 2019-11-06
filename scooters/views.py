from rest_framework import viewsets
from scooters.models import Scooter
from scooters.scooter_serializer import ScooterSerializer
from rest_framework import permissions


class ScooterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class ScooterModelViewSet(viewsets.ModelViewSet):
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer
    permission_classes = (ScooterPermission,)
