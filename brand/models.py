import os
from uuid import uuid4
from django.db import models

# Create your models here.

def brand_logo_file_path(instance, filename):
    """Generate file path for brand logo"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "category", filename)

class Brand(models.Model):
    """Brand Model"""
    title = models.CharField(max_length=72)
    logo = models.ImageField(null=False, upload_to=brand_logo_file_path)