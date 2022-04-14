from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class AboutUs(models.Model):
    """
    About Us.
    """
    title = models.CharField('About us', max_length=50)
    description = RichTextUploadingField(blank=True)

    class Meta:
        verbose_name_plural = 'about us'


class AboutUsImage(models.Model):
    """
    About Us images setting class.
    """
    about = models.ForeignKey(AboutUs, default=None,
                              on_delete=models.CASCADE,
                              null=True, related_name='image')
    image = models.ImageField(upload_to='media/about_us/%Y/%m/%d')

    def clean(self):
        if len(AboutUsImage.objects.filter(about=self.about)) >= 3:
            raise ValidationError("No more than 3 images per item")

    def __str__(self):
        return self.about.title
