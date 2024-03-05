from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, SensorDataViewSet, TokenCreateView

router = DefaultRouter()
router.register('sensors', SensorViewSet, basename="sensors")
router.register('sensor-data', SensorDataViewSet, basename='sensor-data')
router.register('token', TokenCreateView, basename='token-create')

urlpatterns = router.urls
