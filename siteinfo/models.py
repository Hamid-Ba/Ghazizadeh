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


class Ticket(models.Model):
    """Ticket Model"""

    full_name = models.CharField(max_length=125, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    text = models.CharField(max_length=500, null=False, blank=False)
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"


class HomeHeader(models.Model):
    """Home Header"""

    header = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    )

    heading = models.CharField(max_length=72, null=True, blank=True)
    paragraph = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "homeheader"
        verbose_name_plural = "Home Header"


class Footer(models.Model):
    """Footer"""

    heading = models.CharField(max_length=72, null=True, blank=True)
    paragraph = models.CharField(max_length=300, null=True, blank=True)

    # instagram = models.URLField(
    #     max_length=250,
    #     blank=True,
    #     null=True,
    #     error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    # )

    # tweeter = models.URLField(
    #     max_length=250,
    #     blank=True,
    #     null=True,
    #     error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    # )

    # telegram = models.URLField(
    #     max_length=250,
    #     blank=True,
    #     null=True,
    #     error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    # )

    is_active = models.BooleanField(default=False)


class SliderAndBanner(models.Model):
    """Banner"""

    image = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    )

    heading = models.CharField(max_length=100, null=True, blank=True)
    paragraph = models.CharField(max_length=125, null=True, blank=True)
    link_text = models.CharField(max_length=72, null=True, blank=True)

    link_url = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    )

    is_slider = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Slider & Banner"
        verbose_name_plural = "Slider & Banner"


class FAQCategory(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name="faqs")
    question = models.CharField(max_length=500)
    answer = RichTextField()

    def __str__(self):
        return self.question
