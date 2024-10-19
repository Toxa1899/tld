from rest_framework.response import  Response
from django.shortcuts import render
from rest_framework.views import  APIView
from ..map.models import UserLocation
from .serializers import StatisticSerializer
from rest_framework import mixins, viewsets
# Create your views here.

class StatisticAPIView(APIView):
    def get(self, request , uuid):
        queryset = UserLocation.objects.filter(company=uuid)
        serializer = StatisticSerializer(queryset, many=True)
        return  Response(serializer.data)