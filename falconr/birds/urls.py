from rest_framework import routers
from .views import BirdViewSet

router = routers.SimpleRouter()
router.register(r'', BirdViewSet)

urlpatterns = router.urls