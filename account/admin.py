"""
Account Module Admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdminModel

from account.models import User

# Register your models here.


class UserAdmin(BaseAdminModel):
    list_display = ["first_name","last_name", "phone", "is_active", "last_login"]
    list_editable = ["is_active"]
    readonly_fields = ["last_login"]
    list_display_links = ["first_name","last_name", "phone"]
    ordering = ["id"]

    list_filter = ["is_active", "is_staff"]
    search_fields = ["phone"]

    fieldsets = (
        ("General Info", {"fields": ("first_name","last_name", "phone","email","national_code", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        ("General Info", {"fields": ("first_name","last_name", "phone","email","national_code", "password1", "password2")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
