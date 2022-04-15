from django.db import models
from django.contrib.auth.models import User
from ..products.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='favorite')

    def save(self):
        """
        Save 'is favorite' checkbox as True, when product added
        to favorites.
        """
        product = Product.objects.get(pk=self.product_id)
        product.is_favorite = True
        product.save()
        super(Favorite, self).save()

    def __str__(self):
        return self.product.name

