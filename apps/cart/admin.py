from django.contrib import admin
from django.utils.html import format_html

from .models import Cart, CartItem


class CartItemAdmin(admin.StackedInline):
    readonly_fields = [field.name for field in CartItem._meta.fields
                       if not field.name == 'size_line_number']
    exclude = ['size_line_number', 'image']

    def get_image(self, obj):
        return obj.product.images.first().image_tag()

    get_image.short_description = 'Product Image'

    readonly_fields += ['get_image', ]

    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Cart._meta.fields]
    readonly_fields += ['user_details']
    list_display = [field.name for field in Cart._meta.fields]
    inlines = [CartItemAdmin]
    search_fields = ['user__username', 'user__last_name', 'user__email', 'user__phone']
