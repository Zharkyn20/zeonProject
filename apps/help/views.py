from .models import Help
from rest_framework import viewsets
from .serializers import HelpSerializer


class HelpViewSet(viewsets.ModelViewSet):
    """
    Get Help information (1 image, multiple questions)
    """
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
