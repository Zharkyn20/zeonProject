from django.db import models
from django.contrib.auth.models import AbstractUser, User
from ..products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

'''
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)'''


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='favorite')

    def save(self, *args, **kwargs):
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
