from rest_framework import serializers
from .models import Chat, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        print('zx--------------------')
        print(user)
        print(user.id,'----')
        validated_data['my_id'] = user.id
        return Chat.objects.create(**validated_data)





class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, attrs):
        pass