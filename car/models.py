import os
from ckeditor.fields import RichTextField
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

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

    title = models.CharField(max_length=150, verbose_name="عنوان")
    desc = RichTextField(blank=True, null=True, verbose_name="توضیحات")
    image = models.ImageField(null=False, upload_to=car_image_file_path, verbose_name="تصویر")

    gallery = models.ManyToManyField(gallery_models.Gallery, related_name="cars", verbose_name="گالری")
    brand = models.ForeignKey(
        brand_models.Brand, on_delete=models.CASCADE, related_name="cars", verbose_name="برند"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("ماشین")
        verbose_name_plural = _("ماشین ها")


class Car_Specification(models.Model):
    """Specifications Model"""

    key = models.CharField(max_length=125, null=False, blank=False, verbose_name="مشخصه")
    value = models.CharField(max_length=225, null=False, blank=False, verbose_name="مقدار")

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="specs", verbose_name="ماشین")

    def __str__(self):
        return f"{self.car.title}-{self.key}"
    
    class Meta:
        verbose_name = _("مشخصه ماشین")
        verbose_name_plural = _("مشخصات ماشین ها")
