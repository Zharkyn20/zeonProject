from django.db import models


class Help(models.Model):
    """
    Help Image
    """
    image = models.ImageField(upload_to='media/products/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'help'

    def __str__(self):
        return "Help"


class HelpDetails(models.Model):
    """
    Help.
    """
    help_image = models.ForeignKey(Help, on_delete=models.CASCADE,
                                   related_name='help')
    question = models.TextField()
    answer = models.TextField()
