from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Offer(models.Model):
    """
    Offer.
    """
    title = models.CharField(max_length=150)
    description = RichTextUploadingField()

    class Meta:
        verbose_name_plural = 'offer'
