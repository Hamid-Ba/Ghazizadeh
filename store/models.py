import os
from uuid import uuid4
from django.db import models

# Create your models here.


def category_logo_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "category", filename)


class Category(models.Model):
    """Category Model"""

    title = models.CharField(max_length=72, null=False, blank=False)
    logo = models.ImageField(null=False, upload_to=category_logo_file_path)
    order = models.IntegerField(default=1)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_categories",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
