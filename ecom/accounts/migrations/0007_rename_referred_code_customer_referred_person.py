# Generated by Django 5.0.3 on 2024-05-12 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_customer_referred_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="referred_code",
            new_name="referred_person",
        ),
    ]
