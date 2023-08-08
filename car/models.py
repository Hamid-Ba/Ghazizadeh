import os
from ckeditor.fields import RichTextField
from uuid import uuid4

from django.db import models

from brand import models as brand_models
from gallery import models as gallery_models

def car_image_file_path(instance, filename):
    """Generate file path for category image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "car", filename)

# Create your models here.
class Car(models.Model):
    """Car Model"""
    title = models.CharField(max_length=150)
    desc = RichTextField(blank=True, null=True)
    image = models.ImageField(null=False, upload_to=car_image_file_path)
    
    gallery = models.ManyToManyField(gallery_models.Gallery, related_name="cars")
    brand = models.ForeignKey(brand_models.Brand,on_delete=models.CASCADE,related_name="cars")
    
    def __str__(self):
        return self.title
    

class Car_Specification(models.Model):
    """Specifications Model"""

    key = models.CharField(max_length=125, null=False, blank=False)
    value = models.CharField(max_length=225, null=False, blank=False)

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="specs")

    def __str__(self):
        return f"{self.product.title}-{self.key}"