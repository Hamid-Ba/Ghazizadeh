"""
Payment Models Module
"""
from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings

from store import models as store_models


class Payment(models.Model):
    """Payment Model"""

    class PaymentStatus(models.IntegerChoices):
        """Payment Status Enums"""

        PAYMENT_CREATED = 1, "در حال پرداخت"
        PAYMENT_DONE = 2, "پرداخت انجام شد"
        PAYMENT_CANCELLED = 3, "پرداخت لغو شد"

    pay_amount = MoneyField(
        max_digits=10, decimal_places=0, default_currency="IRR", null=False
    )
    desc = models.CharField(max_length=125, null=True, blank=True)
    ref_id = models.CharField(max_length=50, null=True, blank=True)
    authority = models.CharField(max_length=50, null=True, blank=True)
    is_payed = models.BooleanField(default=False)
    payed_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=PaymentStatus.choices, default=PaymentStatus.PAYMENT_CREATED
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payments",
    )
    order = models.ForeignKey(
        store_models.Order, on_delete=models.CASCADE, related_name="payments"
    )

    def __str__(self) -> str:
        return f"User Phone : {self.user.phone}"
