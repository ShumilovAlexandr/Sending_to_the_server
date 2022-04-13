from rest_framework import serializers
from .models import Mailing, Client, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer()
    client = ClientSerializer()

    class Meta:
        model = Message
        fields = '__all__'
