from rest_framework import routers
from .api import PetViewSet

router = routers.DefaultRouter()
router.register('pets', PetViewSet, 'pets')

urlpatterns = router.urls


urlpatterns = router.urls
