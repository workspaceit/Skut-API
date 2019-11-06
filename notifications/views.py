from rest_framework import viewsets
from notifications.models import Notification
from notifications.notificaiton_serializer import NotificationSerializer
from rest_framework import permissions


class NotificationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (NotificationPermission, )
