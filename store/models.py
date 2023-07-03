import os
from uuid import uuid4
from django.db import models
from djmoney.models.fields import MoneyField

from brand import models as brand_models
from gallery import models as gallery_models

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


class Product(models.Model):
    """Product Model"""

    title = models.CharField(max_length=125, null=False, blank=False)
    price = MoneyField(
        max_digits=12, decimal_places=0, default_currency="IRR", null=False
    )
    desc = models.TextField()
    count = models.IntegerField(default=0)
    order_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    gallery = models.ManyToManyField(gallery_models.Gallery, related_name="products")

    brand = models.ForeignKey(
        brand_models.Brand, on_delete=models.CASCADE, related_name="products"
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.title

    def ordered(self, count):
        self.order_count += count
        self.save()


class Specifications(models.Model):
    """Specifications Model"""

    key = models.CharField(max_length=125, null=False, blank=False)
    value = models.CharField(max_length=225, null=False, blank=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")

    def __str__(self):
        return f"{self.product.title}-{self.key}"
