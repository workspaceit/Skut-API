from rest_framework.routers import SimpleRouter
from scooter_models.views import ScooterModelViewSet


router = SimpleRouter()
router.register('', ScooterModelViewSet)

scooter_model_urs = router.urls
