# Generated by Django 4.1 on 2023-07-03 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_blog_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Blog Categories"},
        ),
    ]