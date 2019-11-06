from rest_framework.routers import SimpleRouter
from settings.views import SettingViewSet


router = SimpleRouter()
router.register('', SettingViewSet)

setting_url = router.urls
