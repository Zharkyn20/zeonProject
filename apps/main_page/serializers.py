from rest_framework import serializers
from .models import Slider
from ..products.models import Product
from ..products.serializers import ProductColorSerializer,\
    ProductImageSerializer
from .models import OurAdvantages


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('image', 'url')


class ProductsSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    colors = ProductColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'images', 'name', 'price',
                  'sale_price', 'sale', 'size_line',
                  'colors', 'is_favorite')


class OurAdvantageSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurAdvantages
        fields = ('icon', 'title', 'description')
