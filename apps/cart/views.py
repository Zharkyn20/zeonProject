from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CartSerializer, CartItemSerializer, OrderCartProductsSerializer
from .models import CartItem, Cart


class CartViewSet(viewsets.ModelViewSet):
    """
    Get all existing carts.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True)
    def products(self, request, pk):
        """
        Get all products of some cart. Input: cart id.
        """
        cart = self.get_object()
        products = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def order_cart(self, request, pk):
        """
        Get order information of some cart. Input: cart id.
        """
        cart = self.get_object()
        products = CartItem.objects.filter(cart_id=cart)
        cart.size_line_number = products.count()
        products_total_quantity = 0
        products_total_price = 0
        products_sale_difference = 0
        total_price_after_sale = 0
        for product in products:
            product_quantity = product.size_line_number * product.quantity
            products_total_quantity += product_quantity
            products_total_price += product_quantity * product.price
            products_sale_difference += (product.price - product.sale_price) \
                                        * product.quantity
            total_price_after_sale += product.sale_price * product_quantity
        cart.products_quantity = products_total_quantity
        cart.products_quantity = products_total_quantity
        cart.total_price = products_total_price
        cart.sale = products_sale_difference
        cart.total_price_after_sale = total_price_after_sale
        serializer = OrderCartProductsSerializer(cart)
        return Response(serializer.data)



