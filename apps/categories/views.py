from rest_framework.decorators import action
from .models import Category
from rest_framework import viewsets
from .serializers import CategorySerializer
from ..products.models import Product
from rest_framework.response import Response
from .service import PaginationCategories, PageNumberPagination
from ..products.serializers import SimilarProductsSerializer as CategoryProductsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Get all categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationCategories

    @action(detail=True)
    def products(self, request, pk):
        """
        Get products of some category. Input: category id.
        """
        paginator = PageNumberPagination()
        paginator.page_size = 12
        category = self.get_object()
        products = Product.objects.all().filter(category_id=category.id)
        result = paginator.paginate_queryset(products, self.request)
        serializer = CategoryProductsSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True)
    def novelties(self, request, pk):
        """
        Get novelty products of some category. Input: category id.
        """
        category = self.get_object()
        novelties = Product.objects.all().filter(category_id=category.id).filter(is_novelty=True).order_by('-id')[:5]
        serializer = CategoryProductsSerializer(novelties, many=True)
        return Response(serializer.data)
