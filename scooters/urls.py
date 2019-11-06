from rest_framework.routers import SimpleRouter
from scooters.views import ScooterModelViewSet


router = SimpleRouter()
router.register('', ScooterModelViewSet)

scooter_urs = router.urls
