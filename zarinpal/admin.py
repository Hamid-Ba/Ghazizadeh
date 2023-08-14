from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    """Payment admin"""

    list_display = [
        "user",
        "order",
        "pay_amount",
        "ref_id",
        "is_payed",
        "status",
        "payed_date",
        "created_date",
    ]
    list_display_links = ["user", "order", "pay_amount", "created_date"]
    ordering = ["id"]

    search_fields = ["user__phone", "user__first_name", "user__last_name"]


admin.site.register(Payment, PaymentAdmin)