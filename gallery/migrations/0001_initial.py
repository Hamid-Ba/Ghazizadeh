# Generated by Django 4.1 on 2023-06-10 21:06

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=125, null=True)),
                (
                    "image",
                    models.ImageField(upload_to=gallery.models.gallery_image_file_path),
                ),
            ],
            options={
                "verbose_name_plural": "Galleries",
            },
        ),
    ]
