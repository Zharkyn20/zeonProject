from rest_framework import serializers
from .models import CartItem, Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user')


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    cart_product_color = serializers.SlugRelatedField(slug_field='color', read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ('size_line', 'price', 'sale_price', 'size_line_number', 'image')


class OrderCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('size_line_number', 'products_quantity', 'total_price',
                  'sale', 'total_price_after_sale')
        read_only_fields = ('size_line_number', 'products_quantity', 'total_price',
                            'sale', 'total_price_after_sale')


class CartItemItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ('size_line', 'price', 'sale_price', 'size_line_number', 'image')
