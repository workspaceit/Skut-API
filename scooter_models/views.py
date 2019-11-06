from rest_framework import viewsets
from scooter_models.models import ScooterModel
from scooter_models.scooter_model_serializer import ScooterModelSerializer
from rest_framework import permissions


class ScooterModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class ScooterModelViewSet(viewsets.ModelViewSet):
    queryset = ScooterModel.objects.all()
    serializer_class = ScooterModelSerializer
    permission_classes = (ScooterModelPermission,)
