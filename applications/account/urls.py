from django.urls import path
from .views import RegisterAPIView, ActivateAPIView,UserGetAPIView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('userinfo/', UserGetAPIView.as_view()),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)