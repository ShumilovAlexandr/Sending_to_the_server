from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, MailingViewSet, MessageViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'mailings',  MailingViewSet, basename='mailing')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'clients/<int:pk>', ClientViewSet,
                basename='client_detail')
router.register(r'mailings/<int:pk>', ClientViewSet,
                basename='mailing_detail')

urlpatterns = [
    path(r'', include(router.urls)),
]
