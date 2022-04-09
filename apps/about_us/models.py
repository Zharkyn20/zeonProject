from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField('About us', max_length=50)
    description = RichTextUploadingField(blank=True)


class AboutImage():
    about = models.ForeignKey(About, default= None, on_delete=models.CASCADE, null=True, related_name='image')
    image = models.ImageField(upload_to='media/about/%Y/%m/%d')

    def clean(self):
        if len(AboutImage.objects.filter(product=self.product)) >= 3:
            raise ValidationError("No more than 3 images per item")

    def __str__(self):
        return self.about.title
