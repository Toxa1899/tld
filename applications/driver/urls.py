from django.urls import path
from .views import DriverAView

urlpatterns = [
    path('driver/', DriverAView.as_view())
]
