from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    Get all news.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
