from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  .serializer import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from  rest_framework.authentication import get_user_model
from .serializer import DriverGEtSerializers , DriverSerializer
# Create your views here.

User = get_user_model()

class DriverAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self ,request):
        serializer = DriverSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request):
        # driver = User.objects.all()

        company_user = CompanyUser.objects.filter(company__id=request.data['id_company'])
        serializer = DriverGEtSerializers(company_user, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


    # def get(self, request, pk, format=None):
    #     obj = User.objects.all()
    #     serializer = DriverGEtSerializers(obj)
    #
    #     return Response(serializer.data)

# class Driver
