from django.urls import path
from rest_framework.routers import SimpleRouter
from users.views import UserViewSet, UserInfo
from django.views.decorators.csrf import csrf_exempt


router = SimpleRouter()
router.register('', UserViewSet)

user_urls = [path('info/', UserInfo.as_view())] + router.urls
