"""
Blog Module Models
"""
import os
from uuid import uuid4
from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

from gallery import models as gallery_models


def blog_image_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "blogs", filename)


def blog_category_image_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "blogs", "category", filename)


class BlogCategory(models.Model):
    """Blog Category Model"""

    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    # image = models.ImageField(null=False, upload_to=blog_category_image_file_path)
    image_alt = models.CharField(max_length=72, blank=True, null=True)
    image_title = models.CharField(max_length=125, blank=True, null=True)

    sub_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_categories",
    )
    image = models.ForeignKey(
        gallery_models.Gallery,
        on_delete=models.DO_NOTHING,
        related_name="blog_categories",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Blog Categories"


class Blog(models.Model):
    """Blog Model"""

    title = models.CharField(max_length=85, blank=False, null=False)
    slug = models.SlugField(max_length=170, blank=False, null=False)
    short_desc = models.CharField(max_length=300, blank=True, null=True)
    desc = RichTextField(blank=True, null=True)
    # image = models.ImageField(null=False, upload_to=blog_image_file_path)
    image_alt = models.CharField(max_length=72, blank=True, null=True)
    image_title = models.CharField(max_length=125, blank=True, null=True)
    publish_date = models.DateTimeField(
        null=False, blank=False, default=timezone.now, db_index=True
    )

    tags = TaggableManager(blank=True)
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, related_name="blogs"
    )
    image = models.ForeignKey(
        gallery_models.Gallery,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="blogs",
    )

    def __str__(self) -> str:
        return self.title


class Specification(models.Model):
    """Specification"""

    class Type(models.TextChoices):
        TS = "TS", "مشخصات فنی"
        FE = "FE", "امکانات و تجهیزات"

    type = models.CharField(max_length=2, default=Type.TS, choices=Type.choices)
    key = models.CharField(max_length=125, null=False, blank=False)
    value = models.TextField(null=False, blank=False)

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="specs")

    def __str__(self):
        return f"{self.blog.title}-{self.key}"
