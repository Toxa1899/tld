from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLocationModelViewSet

router = DefaultRouter()
router.register(r'locations', UserLocationModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
