from django.db import models
from .validators import validate_file_extension


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
