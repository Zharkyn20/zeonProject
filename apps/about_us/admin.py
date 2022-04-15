from django.contrib import admin
from .models import AboutUs, AboutUsImage
from . import models


class AboutUsImageAdmin(admin.TabularInline):
    model = AboutUsImage
    max_num = 3


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageAdmin]

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and models.AboutUs.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = AboutUs
