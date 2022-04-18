from rest_framework import viewsets
from .models import FloatingButton, Callback
from .serializers import FloatingButtonSerializer, \
    CallbackSerializer


class FloatingButtonViewSet(viewsets.ModelViewSet):
    """
    Get all WhatsApp and Telegram links.
    """
    queryset = FloatingButton.objects.all()
    serializer_class = FloatingButtonSerializer


class CallbackViewSet(viewsets.ModelViewSet):
    """
    Get Callbacks
    """
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer
