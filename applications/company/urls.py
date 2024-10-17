from django.urls import path
from .views import CompanyView, index, CompanyActivateAPIView, CompanyDeleteAPIView, CompanyUserAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CompanyView.as_view()),
    path('activate/<uuid:activation_code>/', CompanyActivateAPIView.as_view()),
    path('delete/<uuid:delete_code>/', CompanyDeleteAPIView.as_view()),
    path('user/', CompanyUserAPIView.as_view()),

    # path('index/', index)


]
