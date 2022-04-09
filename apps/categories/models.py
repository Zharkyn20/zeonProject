from django.db import models


class Category(models.Model):
    """
    Category model.
    """
    name = models.CharField('Category name', max_length= 50)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'categories'


