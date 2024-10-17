from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  .serializer import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.


class DriverView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self ,request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    