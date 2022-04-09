
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer, SimilarProductsSerializer


class SalePrice:
    """
    Calculates all products' sale price.
    Then sets that value in 'sale_price' products' model field.
    """
    queryset = Product.objects.all()

    for product in queryset:
        product.sale_price = product.get_sale()
        product.save()


class ProductListViewSet(viewsets.ModelViewSet):
    """
    Gets all products list. Descended order by id.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True)
    def similars(self, request, pk):
        """
        Gets 5 similar products. Url: products/id/similars.
        """
        product = self.get_object()
        category = product.category
        queryset = Product.objects.filter(category=category).exclude(id=pk).order_by('-id')[:5]
        serializer = SimilarProductsSerializer(queryset, many=True)
        return Response(serializer.data)
