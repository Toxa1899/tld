from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatModelViewSet, MessageModelViewSet


router = DefaultRouter()
router.register('create_chat', ChatModelViewSet)
router.register('message', MessageModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("create_chat/", ChatAPIViews.as_view()),
    #  path("message/", MessageAPIViews.as_view())
]