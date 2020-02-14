from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('residents', views.ResidentViewSet)

urlpatterns = [] + router.urls
