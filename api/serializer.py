from rest_framework import serializers
from whatsapp.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 1