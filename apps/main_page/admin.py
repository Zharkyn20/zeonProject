from django.contrib import admin
from .models import Slider, OurAdvantages
from django.utils.html import format_html


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}/>'.format(
            url=obj.image.url,
            width=150,
            height=150))

    image_tag.short_description = 'Image'

    readonly_fields = ['image_tag', ]

    class Meta:
        model = Slider

admin.site.register(OurAdvantages)
