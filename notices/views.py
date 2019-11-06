from rest_framework import viewsets
from notices.models import Notice
from notices.notice_serializer import NoticeSerializer
from rest_framework import permissions


class NoticePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (NoticePermission, )
