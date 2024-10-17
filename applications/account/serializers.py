from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tasks import send_activation_code
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError

User = get_user_model()


class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)
    company = serializers.CharField(required=True) 
    usdot = serializers.CharField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
   
    

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'phone', 'company', 'usdot',
                  'number_employees', 'first_name', 'last_name')
        
    
    def validate(self, attrs):

        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        print(p1)
        print(p2)

        if p1 != p2:
            raise serializers.ValidationError('the password does not match ')
        
        try:
            validate_password(p1)
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return attrs
   

    
    # def validate_number_employees(self, number_employees):
    #     if len(str(number_employees)) < 1:
    #          return serializers.ValidationError('в компании не может быть меньше одного работника')
    #     return number_employees
    

    
    def validate_phone(self, phone):
        if phone:
            print()
            if phone[0] == '+' or type(phone[0]) == int:
                print('')
                if not phone[1:].isdigit():
                    raise serializers.ValidationError('phone number cannot contain letters')
            else:
                raise serializers.ValidationError('phone number cannot contain letters')
        return phone
    
    


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code.delay(user.email, user.activation_code,
                                   user.first_name, user.last_name, user.phone,
                                   user.company, user.usdot, user.number_employees)
        return user


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        exclude = ['password', 'activation_code']