"""
Blog Module Models
"""
import os
from django.conf import settings
from uuid import uuid4
from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


def blog_image_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "blogs", filename)

def blog_category_image_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "blogs","category", filename)

class Category(models.Model):
    """Blog Category Model"""
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    image = models.ImageField(null=False, upload_to=blog_category_image_file_path)
    image_alt = models.CharField(max_length=72, blank=False, null=False)
    image_title = models.CharField(max_length=125, blank=False, null=False)
    sub_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Blog(models.Model):
    """Blog Model"""

    title = models.CharField(max_length=85, blank=False, null=False)
    slug = models.SlugField(max_length=170, blank=False, null=False)
    short_desc = models.CharField(max_length=300, blank=False, null=False)
    desc = RichTextField(blank=False, null=False)
    image = models.ImageField(null=False, upload_to=blog_image_file_path)
    image_alt = models.CharField(max_length=72, blank=False, null=False)
    image_title = models.CharField(max_length=125, blank=False, null=False)
    publish_date = models.DateTimeField(null=False, blank=False, default=timezone.now)
    is_cafe = models.BooleanField()

    tags = TaggableManager()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog"
    )

    def __str__(self) -> str:
        return self.title
