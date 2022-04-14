from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
