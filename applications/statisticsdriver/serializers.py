from rest_framework import  serializers

from applications.map.models import UserLocation


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
