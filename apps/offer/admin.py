from django.contrib import admin
from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        # check if generally has added permission
        has_add = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if has_add and Offer.objects.exists():
            has_add = False
        return has_add

    class Meta:
        model = Offer
