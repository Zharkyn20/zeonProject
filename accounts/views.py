from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Get User's information.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
