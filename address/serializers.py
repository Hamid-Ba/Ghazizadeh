from rest_framework import serializers

from address import models


class AddressSerializer(serializers.ModelSerializer):
    """Address Serializer"""

    class Meta:
        model = models.Address
        fields = "__all__"
