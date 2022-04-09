from django.contrib import admin
from .models import Product, ProductImage, ProductColor


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductColorAdmin(admin.StackedInline):
    model = ProductColor


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['sale_price', 'is_favorite']
    inlines = [ProductImageAdmin, ProductColorAdmin]

    class Meta:
        model = Product
