from django.db import models
from .validators import validate_file_extension


# Create your models here.
class MainPage(models.Model):

    class Meta:
        verbose_name_plural = 'Main Page'

    def __str__(self):
        return 'Main Page'


class Slider(models.Model):
    """
    Slider.
    """
    image = models.ImageField(upload_to='media/slider/%Y/%m/%d')
    url = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'slider'

    def __str__(self):
        return self.url


class OurAdvantages(models.Model):
    """
    Our Advantages.
    """
    icon = models.FileField(".svg, .png formats required",
                            upload_to='media/our_advantages/%Y/%m/%d',
                            validators=[validate_file_extension])
    title = models.CharField('Advantage', max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'our advantages'

    def __str__(self):
        return self.title
