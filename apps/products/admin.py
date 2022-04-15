from django.contrib import admin
from .models import Product, ProductImage, ProductColor


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 8


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    max_num = 8


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['sale_price', 'is_favorite']
    # Color and Image Fields for product model.
    inlines = [ProductImageInline, ProductColorInline]

    class Meta:
        model = Product
