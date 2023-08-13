import os
from uuid import uuid4
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField

from brand import models as brand_models
from gallery import models as gallery_models

# Create your models here.


def category_logo_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "category", filename)


class CategoryManager(models.Manager):
    """Category Manager"""

    def get_parents_category(self):
        """return main category"""
        return self.filter(parent=None).order_by("order")


class Category(models.Model):
    """Category Model"""

    title = models.CharField(max_length=72, null=False, blank=False)
    logo = models.ImageField(null=True, blank=True, upload_to=category_logo_file_path)
    order = models.IntegerField(default=1)
    is_cart = models.BooleanField(default=False)

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

    objects = CategoryManager()


class ProductManager(models.Manager):
    """Product Manager"""

    def get_relational_products_by_category(self, product_id, cat_id):
        """return products in same category"""
        return (
            self.filter(category=cat_id, count__gte=3)
            .exclude(id=product_id)
            .order_by("-order_count")
            .values()[:8]
        )


class Product(models.Model):
    """Product Model"""

    title = models.CharField(max_length=125, null=False, blank=False)
    price = MoneyField(
        max_digits=12, decimal_places=0, default_currency="IRR", null=False
    )
    desc = RichTextField(blank=True, null=True)
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

    def get_active_comments(self):
        return self.comments.filter(is_active=True).order_by("create_data").values()

    objects = ProductManager()


class Specifications(models.Model):
    """Specifications Model"""

    key = models.CharField(max_length=125, null=False, blank=False)
    value = models.CharField(max_length=225, null=False, blank=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specs")

    def __str__(self):
        return f"{self.product.title}-{self.key}"


class Comment(models.Model):
    """Commnet Model"""

    full_name = models.CharField(max_length=125, null=False, blank=False)
    text = models.CharField(max_length=750, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    create_data = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self) -> str:
        return f"{self.full_name} commented for {self.product.title}"
