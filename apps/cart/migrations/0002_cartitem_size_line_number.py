# Generated by Django 4.0.3 on 2022-04-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size_line_number',
            field=models.IntegerField(null=True),
        ),
    ]