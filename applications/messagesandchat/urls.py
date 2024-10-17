from django.urls import path
from .views import ChatAPIViews 

urlpatterns = [
    path("create_chat/", ChatAPIViews.as_view()),
     path("message/", ChatAPIViews.as_view())
]