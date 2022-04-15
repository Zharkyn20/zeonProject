from django.contrib import admin
from .models import Cart, CartItem


class CartItemAdmin(admin.StackedInline):
    # These fields would be added by already existing product attributes.
    exclude = ['size_line', 'price', 'sale_price',
               'size_line_number', 'image']
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # These fields would be added by already existing product attributes.
    exclude = ['size_line_number', 'products_quantity',
               'total_price', 'sale', 'total_price_after_sale']
    # Product chooser for cart.
    inlines = [CartItemAdmin]

    class Meta:
        model = Cart
