# Generated by Django 4.0.3 on 2022-04-13 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_line_number', models.IntegerField()),
                ('products_quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('sale', models.IntegerField()),
                ('total_price_after_sale', models.IntegerField()),
                ('user', models.OneToOneField(null=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_line', models.CharField(max_length=150)),
                ('price', models.IntegerField(null=True)),
                ('sale_price', models.IntegerField(blank=True, default=0, verbose_name='Цена после скидки')),
                ('quantity', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='cart.cart')),
                ('cart_product_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product_color', to='products.productcolor')),
                ('cart_product_image', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cart_product_image', to='products.productimage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product')),
            ],
        ),
    ]
