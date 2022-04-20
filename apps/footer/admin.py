from django.contrib import admin
from .models import Footer, Contact
from django.utils.html import format_html


class ContactAdmin(admin.TabularInline):
    model = Contact


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    inlines = [ContactAdmin]

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add

    def icon_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.icon.url,
            width=150,
            height=150))

    icon_tag.short_description = 'Icon'

    readonly_fields = ['icon_tag', ]

    class Meta:
        model = Footer
