"""
site info module models
"""

from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    """About Us Model"""

    title = models.CharField(max_length=125, null=False, blank=False)
    text = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Us"


class ContactUs(models.Model):
    """Contact Us Model"""

    title = models.CharField(max_length=125, null=False, blank=False)
    text = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = "contactus"
        verbose_name_plural = "Contact Us"
