from rest_framework import viewsets, status
from stands.models import Stand
from stands.stand_serializer import StandSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view


class AreaPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return True


class StandViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = (AreaPermission,)


class StandApi:

    @api_view(["get"])
    def get_stands_by_area(request, area_id):
        stands_by_area = Stand.objects.filter(area=area_id)
        list_data = []
        for stand in stands_by_area:
            serializer = StandSerializer(stand)
            list_data.append(serializer.data)
        return Response(data=list_data, status=status.HTTP_200_OK)

