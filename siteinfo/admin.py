"""
site info module admin models
"""
from django.contrib import admin

from siteinfo import models


class AboutUsAdmin(admin.ModelAdmin):
    """About Us Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

    fieldsets = (
        (
            "Main Info",
            {
                "classes": ("collapse",),
                "fields": ("title", "text"),
            },
        ),
    )


class ContactUsAdmin(admin.ModelAdmin):
    """Contact Us Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

    fieldsets = (
        (
            "Main Info",
            {
                "classes": ("collapse",),
                "fields": ("title", "text"),
            },
        ),
    )


admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.ContactUs, ContactUsAdmin)
