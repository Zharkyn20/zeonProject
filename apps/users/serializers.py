from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Favorite
from ..products.models import Product
from ..products.serializers import ProductColorSerializer,\
    ProductImageSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')


class UserFavoritesSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Favorite
        fields = '__all__'


class UserFavoritesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class UserFavoritesProductsSerializer(serializers.ModelSerializer):
    colors = ProductColorSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'sale_price', 'sale', 'size_line',
                  'id', 'is_favorite', 'images', 'colors')