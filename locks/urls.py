from rest_framework.routers import SimpleRouter
from locks.views import LockViewSet


router = SimpleRouter()
router.register('', LockViewSet)

lock_urs = router.urls
