import uuid

from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.company.models import Company, CompanyUser
from applications.account.tasks import send_create_company, send_delete_company
from rest_framework.generics import get_object_or_404
User = get_user_model()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        import uuid

        validated_data['user'] = user
        validated_data['activation_code'] = str(uuid.uuid4())



        company = Company.objects.create(**validated_data)
        CompanyUser.objects.create(company=company, user=user)

        # Отправка уведомления
        send_create_company.delay(
            company.email,
            company.name,
            company.phone,
            company.home_terminal_address,
            company.home_terminal_timezone,
            company.company_address,
            company.user.last_name,
            company.user.first_name,
            company.activation_code
        )
        return company



class CompanyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'id']


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'first_name', 'last_name', 'email', 'phone', 'is_driver']


class CompanyUserGetSerializer(serializers.ModelSerializer):
    company = CompanyGetSerializer()
    user = UserGetSerializer()

    class Meta:
        model = CompanyUser
        fields = ['user', 'company']

from django.contrib.auth import authenticate

class CompanyDELSerializer(serializers.Serializer):
    id_company = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate(self, attrs):
        id_company = attrs.pop('id_company')
        email = attrs.get('email')
        password = attrs.get('password')

        # Проверка на существование компании
        if not Company.objects.filter(id=id_company, is_active=True).exists():
            raise serializers.ValidationError('company not found')

        # Аутентификация пользователя с указанным email и паролем
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid credentials')

        code = str(uuid.uuid4())
        company = Company.objects.filter(id=id_company, user=user).first()
        company_name = company.name
        send_delete_company.delay(company_name, email, code, user.first_name, user.last_name)
        company.delete_code = code
        company.save()





        return attrs



class CompanyAddUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    id_company = serializers.CharField(required=True, write_only=True)


    class Meta:
        model = CompanyUser
        fields = ('id_company', 'email')

    def validate_email(self, email):
        req = self.context.get('request')
        user = CompanyUser.objects.filter(user__email=email, user__is_active=True).exists()
        if not user:
            serializers.ValidationError('User does not exist')
        if req.user.email == email:
            serializers.ValidationError('You cannot add yourself')

        if CompanyUser.objects.filter(user__email=email).exists():
            print(email)
            raise serializers.ValidationError('This user is already present in your company')

        return email

    # def validate(self, attrs):
    #     request = self.context.get('request')

    #     company = get_object_or_404(CompanyUser, user=request.user)
    #     if company.role != 'Owner':
    #         raise serializers.ValidationError('your role is not owner')

        return attrs

    def create(self, validated_data):
        # Получаем связанные объекты User и Company
        user = User.objects.get(email=validated_data['email'])
        company = Company.objects.get(id=validated_data['id_company'])

        # Создаем объект CompanyUser
        company_user = CompanyUser.objects.create(
      
            user=user,
            company=company
        )

        return company_user

    # company = serializers.CharField(max_length=100)
    # role = serializers.CharField(max_length=80)

class CompanyUserSerializer(serializers.ModelSerializer):
    id_company = serializers.CharField(required=True, write_only=True)
    company_user = CompanyUserGetSerializer(read_only=True, many=True,)



    def validate(self, attrs):
        id_company = attrs.pop('id_company')
        company_user = CompanyUser.objects.filter(company__id=id_company)
        attrs['company_user'] = company_user

        request = self.context.get('request')

        # if not CompanyUser.objects.filter(user=request.user, company__id=id_company).exists():
        #     raise serializers.ValidationError('you are not a member of this company')

        return attrs

    class Meta:
        model = CompanyUser
        fields = ('id_company', 'company_user')




        #     company = CompanyGetSerializer(c)

    # def validate_id_company(self, id_company):
    #     c = get_object_or_404(Company, id=id_company)
    #     company = CompanyGetSerializer(c)
    #
    #     return company
    # id = uuid.UUID(id_company).hex
    # c = get_object_or_404(Company, id=id_company)
    # c = Company.objects.get(id=id)

    # company = CompanyGetSerializer(c)
    # first_name = serializers.CharField(source='user.first_name')
    # last_name = serializers.CharField(source='user.last_name')



class CompanyUserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    class Meta:
        model = CompanyUser
        fields = ['role', 'email']


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)

    #

