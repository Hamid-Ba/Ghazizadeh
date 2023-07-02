from rest_framework import serializers

from store import models


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Category
        fields = "__all__"
