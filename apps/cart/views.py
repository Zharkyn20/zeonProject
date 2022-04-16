from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CartSerializer,\
    CartItemSerializer, OrderCartSerializer, \
    PostCartItemSerializer
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
        serializer = OrderCartSerializer(cart)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_classes = {
        'list': CartItemSerializer,
        'create': PostCartItemSerializer,
    }
    default_serializer_class = CartItemSerializer  # Your default serializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)
