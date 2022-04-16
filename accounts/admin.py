from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.cart.models import Cart, CartItem
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'phone', 'country',
        'city'
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional info', {
            'fields': ('phone', 'country', 'city')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
