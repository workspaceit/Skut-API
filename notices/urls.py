from rest_framework.routers import SimpleRouter
from notices.views import NoticeViewSet


router = SimpleRouter()
router.register('', NoticeViewSet)

notice_url = router.urls
