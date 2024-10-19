from django.urls import path, include
from .views import StatisticAPIView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
#
# router.register("", StatisticAPIView)



urlpatterns = [
    path('<uuid:uuid>/', StatisticAPIView.as_view())

]