from rest_framework import viewsets
from areas.models import Area
from areas.serializer import AreaSerializer
from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import status

import logging
logger = logging.getLogger(__name__)


class AreaPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


# class AreaViewSet(viewsets.ModelViewSet):
#     queryset = Area.objects.all()
#     serializer_class = AreaSerializer
#     permission_classes = (AreaPermission,)

class AreaList(generics.ListCreateAPIView):
    """
    Return a list of all areas
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(APIView):
    """
    Get area details with guid
    """
    def get_object(self, guid):
        try:
            return AreaDetail.objects.get(guid=guid)
        except AreaDetail.DoesNotExist:
            raise Http404

    def get(self, request, guid, format=None):
        area = self.get_object(guid=guid)
        serializer = AreaSerializer(area)
        return Response(serializer.data)