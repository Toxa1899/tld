from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializers, UserGetSerializer
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from decouple import config
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializers = RegisterSerializers(data=request.data)
        print(request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('You have successfully registered, to activate, check your email', status=201)




class ActivateAPIView(View):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        LINK_LOGIN = config("LINK_RENDER")
        return render(request, 'activation_success.html', context={'LINK_LOGIN': LINK_LOGIN})


class UserGetAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = CustomUser.objects.filter(id=request.user.id).first()
        serializer = UserGetSerializer(user)
        return Response(serializer.data, status=202)