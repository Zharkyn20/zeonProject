from django.core.exceptions import ValidationError
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from apps.categories.models import Category
from colorfield.fields import ColorField


class Product(models.Model):
    """
    Product.
    """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='product')
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)    # Артикул товара
    price = models.IntegerField()
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    sale_price = models.IntegerField('Цена после скидки', blank=True, default=0)
    description = RichTextUploadingField(blank=True)
    size_line = models.CharField(max_length=150)
    size_line_number = models.IntegerField()
    fabric_structure = models.TextField()
    material = models.CharField(max_length=100)
    is_best_seller = models.BooleanField(default=False)
    is_novelty = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ('-id',)

    def get_sale(self):
        """
        Function that gets product's price after sale. Further this value sets to the
        'sale_price' product model's field.
        """
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def save(self):
        self.sale_price = self.get_sale()
        super(Product, self).save()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    Product images setting class.
    """
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, null=True, related_name='images')
    image = models.ImageField(upload_to='media/products/%Y/%m/%d')

    def __str__(self):
        return self.image.url


class ProductColor(models.Model):
    """
    Product colors setting class.
    """
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='colors')
    color = ColorField(default='#FF0000')

    def clean(self):
        if len(ProductColor.objects.filter(product=self.product)) >= 8:
            raise ValidationError("No more than 8 images per item")

    def __str__(self):
        return f"{self.product} {self.color}"
