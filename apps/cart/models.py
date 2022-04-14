from django.db import models
from django.contrib.auth.models import User
from ..products.models import Product, ProductColor, ProductImage


class Cart(models.Model):
    """
    Cart. One user could have only one cart. No cart without user (this
    function may be added in the future versions).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=1)
    size_line_number = models.IntegerField()
    products_quantity = models.IntegerField()
    total_price = models.IntegerField()
    sale = models.IntegerField()
    total_price_after_sale = models.IntegerField()

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    """
    Cart items.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='cart_item', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product')
    cart_product_image = models.ForeignKey(ProductImage,
                                           on_delete=models.CASCADE,
                                           related_name='cart_product_image',
                                           default=None)
    cart_product_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='cart_product_color')
    size_line = models.CharField(max_length=150)
    size_line_number = models.IntegerField()
    price = models.IntegerField(null=True)
    sale_price = models.IntegerField('Цена после скидки', blank=True, default=0)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    """
    Get Product's and assigns to cart item's attributes.
    """
    def get_product_params(self):
        product = Product.objects.get(pk=self.product_id)
        size_line = product.size_line
        size_line_number = product.size_line_number
        price = product.price
        sale_price = product.sale_price
        result = {1: size_line, 2: price, 3: sale_price,
                  4: size_line_number}
        return result

    """
    Saves cart item's assigned attributes.
    """
    def save(self, *args, **kwargs):
        product = self.get_product_params()
        self.size_line = product[1]
        self.price = product[2]
        self.sale_price = product[3]
        self.size_line_number = product[4]
        super(CartItem, self).save()

    def __str__(self):
        return str(self.product.name)
