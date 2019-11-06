from rest_framework import viewsets, status
from scooter_categories.models import ScooterCategory
from scooter_categories.scooter_category_serializer import ScooterCategorySerializer
from rest_framework import permissions


class ScooterCategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class ScooterCategoryViewSet(viewsets.ModelViewSet):
    queryset = ScooterCategory.objects.all()
    serializer_class = ScooterCategorySerializer
    permission_classes = (ScooterCategoryPermission,)
