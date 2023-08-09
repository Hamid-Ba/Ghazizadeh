# Generated by Django 4.1 on 2023-08-08 17:55

import car.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(
                default="test", upload_to=car.models.car_image_file_path
            ),
            preserve_default=False,
        ),
    ]