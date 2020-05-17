from rest_framework import routers
from .api import TestViewSet

router = routers.SimpleRouter()
router.register('api/test', TestViewSet, 'test_app')

urlpatterns = router.urls
