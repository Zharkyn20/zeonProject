from django.contrib import admin
from .models import Footer, Contact


class ContactAdmin(admin.TabularInline):
    model = Contact


@admin.register(Footer)
class CartAdmin(admin.ModelAdmin):
    inlines = [ContactAdmin]

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = Footer
