from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ChatAPIViews(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChatSerializer(data=request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Great")


class MessageAPIViews(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = MessageSerializer(data=request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("success")