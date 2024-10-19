
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  viewsets
from rest_framework.decorators import authentication_classes, action
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ChatModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    @action(detail=False, methods=['POST'])
    def post(self, request):
        serializer = ChatSerializer(data=request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Great")


class MessageModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


    @action(detail=False, methods=['POST'])
    def post(self, request):
        serializer = MessageSerializer(data=request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("success")