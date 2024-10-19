from xml.dom import registerDOMImplementation

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from urllib3 import request

from applications.account.models import CustomUser
from applications.account.serializers import UserGetSerializer
from applications.company.models import Company, CompanyUser
from django.db.models import Q
# from applications.account import *


User = get_user_model()

class DriverSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)
    vin = serializers.CharField()
    drivers_license = serializers.CharField()
    drivers_license_issuing_state = serializers.ChoiceField(choices=CustomUser.DRIVERS_LICENSE_ISSUING_STATE_CHOICES)
    home_terminal_address = serializers.CharField()
    company = serializers.CharField()




    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'first_name', 'last_name' ,'username', 
                  'password', 'password2', 'phone', 'vin', 'drivers_license', 
                  'drivers_license_issuing_state', 'home_terminal_address', 'company']


    def validate(self, attrs):

        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('the password does not match ')

        try:
            validate_password(p1)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return attrs




    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists")
        return  email

    def validate_company(self, company):
        company_e = Company.objects.filter(Q(id=company)).exists()
        if not company_e:
            raise serializers.ValidationError('company not found')
        return  company




    def create(self, validated_data):
        request = self.context.get('request')
        company_e = Company.objects.filter(Q(id=validated_data['company'])).first()
        CompanyUser.objects.create(
            company = company_e,
            user= request.user,
            is_driver= True

        )

        return  CustomUser.objects.create(**validated_data)
        # user.save()

class DriverGEtSerializers(serializers.ModelSerializer):
    id_company = serializers.CharField(required=True, write_only=True)
    user = UserGetSerializer()
    class Meta:
        model = CompanyUser
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     # print(instance['id_company'])
    #     #
    #     # zxc = CompanyUser.objects.filter(company__id='8ae26845-176b-491c-ab72-4eb9825095f1')
    #     # rep['zxc'] = zxc
    #     return rep