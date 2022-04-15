from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, \
    UserFavoritesSerializer, UserFavoritesProductsSerializer
from .models import Favorite
from ..products.models import Product


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
        favorites = Favorite.objects.all().filter(user=user)
        products = []
        for item in favorites:
            product = Product.objects.filter(id=item.product_id)
            products += product
        serializer = UserFavoritesProductsSerializer(products,
                                                     many=True)
        return Response(serializer.data)


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    Get all user's favorite products.
    """
    queryset = Favorite.objects.all()
    serializer_class = UserFavoritesSerializer
