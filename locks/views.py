from rest_framework import viewsets
from locks.models import Lock
from locks.locks_serializer import LockSerializer
from rest_framework import permissions


class LockPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == 'GET' and request.user.has_perm('locks.view_lock'):
                return True
            elif request.method == 'POST' and request.user.has_perm('locks.add_lock'):
                return True
            elif request.method in ['PATCH', 'PUT'] and request.user.has_perm('locks.change_lock'):
                return True
            elif request.method == 'DELETE' and request.user.has_perm('locks.delete_lock'):
                return True
        return False


class LockViewSet(viewsets.ModelViewSet):
    queryset = Lock.objects.all()
    serializer_class = LockSerializer
    permission_classes = (LockPermission,)
