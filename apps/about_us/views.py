from rest_framework import viewsets
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    """
    Get About Us information. Only one object exists.
    """
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

