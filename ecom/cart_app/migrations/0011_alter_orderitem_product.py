# Generated by Django 5.0.3 on 2024-04-17 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0010_remove_product_old_price_product_percentage"),
        ("cart_app", "0010_order_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="admin_app.productcolorimage",
            ),
        ),
    ]
