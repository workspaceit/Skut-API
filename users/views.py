from rest_framework.permissions import BasePermission
from rest_framework import viewsets, status, serializers
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
from users.models import UserProfile
from users.user_serializer import UserProfileSerializer


class UserProfilePermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated:
            if request.user.groups.filter(name='user').exists():
                if request.method in ['GET', 'PUT', 'PATCH'] and view.get_view_name() == 'User Instance'\
                        and request.user.userprofile.uid == request.parser_context.get('kwargs', {}).get('pk'):
                    return True
            elif request.user.groups.filter(name='admin').exists():
                return True
            elif request.user.groups.filter(name='manager').exists():
                return True
        elif request.method == 'POST':
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (UserProfilePermissions,)

    def create(self, request, *args, **kwargs):
        request_type = request.data.pop("request_type", '')
        try:
            if request_type == "login-registration":
                return self.serializer_class.create(UserProfileSerializer(), request.data)
            elif request_type == "submit-reg-code":
                return self.serializer_class.check_registration_code(UserProfileSerializer(), request.data)
            elif request_type == "final-submit":
                return self.serializer_class.final_create(UserProfileSerializer(), request.data)
        except serializers.ValidationError as ex:
            response = exception_handler(ex, {})
            return response
        except Exception as ex:
            print(ex)
        return Response({'status': False, 'message': "Something went wrong."}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        instance = self.serializer_class.update(UserProfileSerializer(), UserProfile.objects.get(pk=kwargs['pk']), request.data)
        serialize_data = self.serializer_class(instance)
        return Response(serialize_data.data, status=status.HTTP_200_OK)


class UserInfo(APIView):
    permission_classes = (UserProfilePermissions, )

    def get(self, request):
        user = UserProfileSerializer(request.user.userprofile)
        return Response(user.data, status=status.HTTP_200_OK)
