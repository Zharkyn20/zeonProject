from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, \
    UserFavoritesSerializer, UserFavoritesProductsSerializer, \
    UserFavoritesPostSerializer
from .models import Favorite
from ..products.models import Product
from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def favorites(self, request, pk):
        """
        Get user's favorite products. Input: user id (for which
        you want to get favorite products).
        """
        user = self.get_object()
        paginator = PageNumberPagination()
        paginator.page_size = 12
        favorites = Favorite.objects.all().filter(user=user)
        products = []
        for item in favorites:
            product = Product.objects.filter(id=item.product_id)
            products += product
        result = paginator.paginate_queryset(products, self.request)
        serializer = UserFavoritesProductsSerializer(result,
                                                     many=True)
        return paginator.get_paginated_response(serializer.data)


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    Get all user's favorite products.
    """
    queryset = Favorite.objects.all()
    serializer_classes = {
        'create': UserFavoritesPostSerializer
    }
    default_serializer_class = UserFavoritesSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
