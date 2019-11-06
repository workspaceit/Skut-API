from rest_framework.routers import SimpleRouter
from scooter_categories.views import ScooterCategoryViewSet


router = SimpleRouter()
router.register('', ScooterCategoryViewSet)

scooter_category_urs = router.urls
