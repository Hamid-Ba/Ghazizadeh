# Generated by Django 4.1 on 2024-05-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0015_alter_orderitem_brand_alter_orderitem_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="weight",
            field=models.FloatField(default=0),
        ),
    ]
