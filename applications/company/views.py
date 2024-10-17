from decouple import config
from django.shortcuts import render
from django.views import View
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from applications.company.models import Company, CompanyUser
from applications.company.serializers import CompanySerializer, CompanyGetSerializer, CompanyDELSerializer, \
    CompanyUserGetSerializer, CompanyUserSerializer, CompanyAddUserSerializer, CompanyUserUpdateSerializer


class CompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = CompanySerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('You have successfully registered a company, to activate, check your email', status=201)

    def get(self, request):
        companies = CompanyUser.objects.filter(user=request.user, company__is_active=True)
        serializer = CompanyUserGetSerializer(companies, many=True)
        return Response(serializer.data)

    def delete(self, request):
        serializers = CompanyDELSerializer(data=request.data, context={''})
        serializers.is_valid(raise_exception=True)
        return Response("An email has been sent to your company's email address to confirm the company's deletion.",status=201)


class CompanyActivateAPIView(View):
    def get(self, request, activation_code):
        companies = get_object_or_404(Company, activation_code=activation_code)
        companies.is_active = True
        companies.owner = True
        companies.activation_code = ''
        companies.save()
        LINK_LOGIN = config("LINK_RENDER")
        return render(request, 'activation_success.html', context={'LINK_LOGIN': LINK_LOGIN})


class CompanyDeleteAPIView(View):
    permission_classes = [IsAuthenticated]

    def get(self, request, delete_code):
        companies = get_object_or_404(Company, delete_code=delete_code)
        companies.is_active = False
        companies.delete_code = ''
        companies.save()
        LINK_LOGIN = config("LINK_RENDER")
        return render(request, 'activation_success.html', context={'LINK_LOGIN': LINK_LOGIN})


class CompanyUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, ):
        serializer = CompanyAddUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('you have successfully added an employee to the company', status=201)


    def get(self, request):
        serializers = CompanyUserSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        return Response(serializers.data)

    def put(self, request):
        serializers = CompanyUserUpdateSerializer(data=request.data, context={'request':request})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('role updated successfully')


def index(request):
    return render(request,'email_template.html')