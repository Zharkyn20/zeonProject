from django.db import models
from ruamel import yaml
from ..products.models import Product, ProductColor, ProductImage
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class StatusChoice(models.TextChoices):
    NEW = u'N', 'New'
    ORDERED = u'O', 'Ordered'
    CANCELLED = u'C', 'Cancelled'


class Cart(models.Model):
    """
    Cart. One user could have only one cart. No cart without user! (this
    function may be added in the future versions).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    size_line_number = models.IntegerField(null=True)
    products_quantity = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    sale = models.IntegerField(null=True)
    total_price_after_sale = models.IntegerField(null=True)
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=StatusChoice.choices,
                              default=StatusChoice.NEW)

    def __str__(self):
        return self.user.username

    def user_details(self):
        result = {
            'Last name': self.user.last_name,
            'Email address': self.user.email,
            'Phone number': str(self.user.phone),
            'Country': self.user.country,
            'City': self.user.city
        }
        return yaml.dump(result, default_flow_style=False)

    def search_fields(self):
        return self.user.username, self.user.phone, \
               self.user.last_name, self.user.email

    def save(self, *args, **kwargs):
        cart_item = CartItem.objects.filter(cart_id=self.id)
        self.size_line_number = cart_item.count()
        result = {1: 0, 2: 0, 3: 0, 4: 0}
        for item in cart_item:
            product_quantity = item.size_line_number * item.quantity
            result[1] += product_quantity
            result[2] += item.price * product_quantity
            result[3] += (item.price - item.sale_price) * product_quantity
            result[4] += item.sale_price * product_quantity
        self.products_quantity = result[1]
        self.total_price = result[2]
        self.sale = result[3]
        self.total_price_after_sale = result[4]
        super(Cart, self).save()


class CartItem(models.Model):
    """
    Cart items.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='cart_item', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product')
    image = models.CharField(max_length=100)
    cart_product_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE,
                                           related_name='cart_product_color')
    size_line = models.CharField(max_length=150)
    size_line_number = models.IntegerField()
    price = models.IntegerField(null=True)
    sale_price = models.IntegerField('Цена после скидки', blank=True, default=0)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    """
    Get Product's and assigns to cart item's attributes.
    """

    def get_product_params(self):
        product = Product.objects.get(pk=self.product_id)
        size_line = product.size_line
        size_line_number = product.size_line_number
        price = product.price
        sale_price = product.sale_price
        image = product.images.first()
        result = {1: size_line, 2: price, 3: sale_price,
                  4: size_line_number, 5: image}
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
        self.image = product[5]
        super(CartItem, self).save()

    def __str__(self):
        return str(self.product.name)
