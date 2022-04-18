from rest_framework import viewsets
from .models import Slider
from ..products.models import Product
from ..categories.models import Category
from ..categories.serializers import CategorySerializer
from .serializers import SliderSerializer, \
    ProductsSerializer, OurAdvantageSerializer
from .service import PaginationMainPage, PaginationCategories
from .models import OurAdvantages


class SliderViewSet(viewsets.ModelViewSet):
    """
    Get all sliders.
    """
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class BestSellerViewSet(viewsets.ModelViewSet):
    """
    Get all bestseller products.
    """
    queryset = Product.objects.filter(is_best_seller=True)
    serializer_class = ProductsSerializer
    pagination_class = PaginationMainPage


class NoveltiesViewSet(viewsets.ModelViewSet):
    """
    Get all novelty products.
    """
    queryset = Product.objects.filter(is_novelty=True)
    serializer_class = ProductsSerializer
    pagination_class = PaginationMainPage


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Get categories, paginated by 4
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationCategories


class MoreCategoriesViewSet(viewsets.ModelViewSet):
    """
    Get categories, paginated by 8
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationMainPage


class OurAdvantagesViewSet(viewsets.ModelViewSet):
    """
    Get 4 Our Advantages.
    """
    queryset = OurAdvantages.objects.all()[:4]
    serializer_class = OurAdvantageSerializer
