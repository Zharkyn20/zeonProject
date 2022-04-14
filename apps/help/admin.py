from django.contrib import admin
from .models import Help, HelpDetails
from . import models


class HelpDetailsAdmin(admin.StackedInline):
    model = HelpDetails


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    inlines = [HelpDetailsAdmin]

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and models.Help.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = Help
