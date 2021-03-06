from rest_framework import serializers
from .models import Product, ProductColor, ProductImage


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('color',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # get colors for product
    colors = ProductColorSerializer(many=True)
    # get images for product
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        read_only_fields = ('sale_price', 'is_favorite')
        fields = '__all__'


class SimilarProductsSerializer(serializers.ModelSerializer):
    # get colors for product
    colors = ProductColorSerializer(many=True)
    # get images for product
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'sale_price', 'sale',
                  'size_line', 'is_favorite', 'images', 'colors')


class SearchProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # get colors for product
    colors = ProductColorSerializer(many=True)
    # get images for product
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        read_only_fields = ('sale_price', 'is_favorite', 'search_input')
        fields = ('id', 'images', 'name', 'price',
                  'sale_price', 'sale', 'size_line',
                  'colors', 'is_favorite',
                  'category')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['search_input'] = self.context['search_input']

        return representation
