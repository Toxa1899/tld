from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from applications.account.models import CustomUser
from applications.company.models import Company
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
    id_company = serializers.CharField()




    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'first_name', 'last_name' ,'username', 
                  'password', 'password2', 'phone', 'vin', 'drivers_license', 
                  'drivers_license_issuing_state', 'home_terminal_address', 'id_company']


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


    def validate_id_company(self, id_company):
        
        company = Company.objects.filter(Q(id=id_company))
        if not company:
            raise serializers.ValidationError('company not found')
        # return name_ore_id_company


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()