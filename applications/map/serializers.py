from rest_framework import serializers
from .models import UserLocation

class UserLocationSerializer(serializers.ModelSerializer):
    company = serializers.UUIDField(required=True)

    class Meta:
        model = UserLocation
        fields = ['id', 'user', 'latitude', 'longitude', 'timestamp', 'company']
        read_only_fields = ['user']
