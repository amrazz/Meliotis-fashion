# Generated by Django 5.0.3 on 2024-04-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="product_size",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
