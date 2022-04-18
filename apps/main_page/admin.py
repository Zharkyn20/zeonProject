from django.contrib import admin
from .models import Slider, OurAdvantages


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    exclude = ['url']

    class Meta:
        model = Slider

admin.site.register(OurAdvantages)