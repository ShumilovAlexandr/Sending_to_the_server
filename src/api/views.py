from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from src.service.models import *
from src.service.serializers import ClientSerializer, \
    MailingSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    filter_backends = [DjangoFilterBackend]
