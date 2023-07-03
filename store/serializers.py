from rest_framework import serializers

from store import models
from brand import serializers as brand_serial
from gallery import serializers as gallery_serial


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Category
        fields = "__all__"


class SpecificationsSerializer(serializers.ModelSerializer):
    """Specifications Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Specifications
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    """Product Serializer"""

    category = CategorySerializer(many=False)
    brand = brand_serial.BrandSerializer(many=False)
    gallery = gallery_serial.GallerySerializer(many=True)

    class Meta:
        """Meta Class"""

        model = models.Product
        fields = ["title", "price", "category", "brand", "gallery"]


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""

    category = CategorySerializer(many=False)
    brand = brand_serial.BrandSerializer(many=False)
    gallery = gallery_serial.GallerySerializer(many=True)
    specs = SpecificationsSerializer(many=True)

    class Meta:
        """Meta Class"""

        model = models.Product
        fields = "__all__"
