from django.db import models


class Slider(models.Model):
    """
    Slider.
    """
    image = models.ImageField(upload_to='media/slider/%Y/%m/%d')
    url = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'slider'

    def save(self):
        self.url = self.image.url
        super(Slider, self).save()

    def __str__(self):
        return self.id
