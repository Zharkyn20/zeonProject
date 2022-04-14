from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    """
    News
    """
    image = models.ImageField(upload_to='media/news/%Y/%m/%d')
    title = models.CharField('News', max_length=100)
    description = RichTextUploadingField()

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

