# Generated by Django 4.1 on 2023-07-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siteinfo", "0002_footer_homeheader_sliderandbanner"),
    ]

    operations = [
        migrations.AddField(
            model_name="footer",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="homeheader",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
