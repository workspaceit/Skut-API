from rest_framework import viewsets
from settings.models import Setting
from settings.settings_serializer import SettingSerializer
from rest_framework import permissions


class SettingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (SettingPermission, )
