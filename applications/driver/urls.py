from django.urls import path
from .views import DriverView

urlpatterns = [
    path('create_driver/', DriverView.as_view())
]
