from django.urls import path
from rest_framework.routers import SimpleRouter
from rides.views import RideViewSet, RideAPi


router = SimpleRouter()
router.register('', RideViewSet)

ride_urls = [
                path('by-user/', RideAPi.ride_history_by_user),
                path('by-scan/', RideAPi.ride_by_scan),
                path('stop-ride/', RideAPi.stop_ride)
             ] + router.urls
