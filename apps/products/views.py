import random

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Product
from ..categories.models import Category
from rest_framework import viewsets
from .serializers import ProductSerializer, SimilarProductsSerializer, \
    SearchProductSerializer
from .service import PaginationProducts


class ProductListViewSet(viewsets.ModelViewSet):
    """
    Get all products list. Descended order by id.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
    pagination_class = PaginationProducts

    @action(detail=True)
    def similars(self, request, name):
        """
        Get 5 similar products. Input: product id (for which
        you want to get similar products).
        """
        product = self.get_object()
        category = product.category
        queryset = Product.objects.filter(category=category).filter(~Q(name=name)).order_by('-id')[:5]
        serializer = SimilarProductsSerializer(queryset,
                                               many=True)
        return Response(serializer.data)

    @action(detail=True)
    def search_results(self, request, *args, **kwargs):
        """
        Search input required. Results shown in separate page
        'search_results'. If input text is similar to product's name
        Output: all products, with pagination (8 objects).
        If input text is not similar to any product:
        Output: 5 products from different categories.
        """
        products = Product.objects.filter(name__contains=kwargs['name'])
        paginator = PageNumberPagination()
        paginator.page_size = 8
        if products.exists():
            result = paginator.paginate_queryset(products, self.request)
            serializer = SearchProductSerializer(result,
                                                 context={'search_input': kwargs['name']},
                                                 many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            categories = Category.objects.all()
            random_products = Product.objects.none()
            category_set = Category.objects.none()
            while random_products.count() < 5:
                category = random.choice(categories)
                if category in category_set:
                    continue
                category_set |= Category.objects.filter(name=category)
                category_products = Product.objects.filter(category__name=category)
                product = random.choice(category_products)
                random_products |= Product.objects.filter(name=product)
            serializer = SearchProductSerializer(random_products,
                                                 context={'search_input': kwargs['name']},
                                                 many=True)
            return Response(serializer.data)
