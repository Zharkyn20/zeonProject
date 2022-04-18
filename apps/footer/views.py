from rest_framework import viewsets
from .models import Footer
from .serializers import FooterSerializer


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer