from django.conf import settings

from django.db import models
from province import models as province_model

class Address(models.Model):
    """Address Model"""

    desc = models.CharField(max_length=225, null=True, blank=True)
    street = models.CharField(max_length=225, null=True, blank=True)
    postal_code = models.CharField(max_length=10)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses"
    )
    province = models.ForeignKey(province_model.Province, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(province_model.City, on_delete=models.DO_NOTHING)
