from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer, SimilarProductsSerializer


class ProductListViewSet(viewsets.ModelViewSet):
    """
    Get all products list. Descended order by id.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True)
    def similars(self, request, pk):
        """
        Get 5 similar products. Input: product id (for which
        you want to get similar products).
        """
        product = self.get_object()
        category = product.category
        queryset = Product.objects.filter(category=category).exclude(id=pk).order_by('-id')[:5]
        serializer = SimilarProductsSerializer(queryset, many=True)
        return Response(serializer.data)
