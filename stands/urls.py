from django.urls import path
from rest_framework.routers import SimpleRouter
from stands.views import StandViewSet, StandApi
from django.views.decorators.csrf import csrf_exempt


router = SimpleRouter()
router.register('', StandViewSet)

stand_urls = [path('by_area/<area_id>/', StandApi.get_stands_by_area)] + router.urls
