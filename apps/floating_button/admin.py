from django.contrib import admin
from .models import FloatingButton, Callback


@admin.register(FloatingButton)
class AboutUsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has add permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and FloatingButton.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = FloatingButton


@admin.register(Callback)
class Callback(admin.ModelAdmin):
    readonly_fields = [field.name for field in Callback._meta.fields]
    search_fields = ['phone', 'name']
    list_filter = ('is_called',)
