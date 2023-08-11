from rest_framework import serializers

from brand import serializers as brand_serial
from gallery import serializers as gallery_serial

from car import models


class SpecificationsSerializer(serializers.ModelSerializer):
    """Specifications Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Car_Specification
        fields = "__all__"


class CarListSerializer(serializers.ModelSerializer):
    """Car List Serializer"""

    brand = brand_serial.BrandSerializer(many=False)

    class Meta:
        model = models.Car
        fields = ["title", "brand", "image"]


class CarSerializer(serializers.ModelSerializer):
    """Car Serializer"""

    brand = brand_serial.BrandSerializer(many=False)
    gallery = gallery_serial.GallerySerializer(many=True)
    specs = SpecificationsSerializer(many=True)

    class Meta:
        """Meta Class"""

        model = models.Car
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     relational_products = (
    #         models.Product.objects.get_relational_products_by_category(
    #             instance.category.id
    #         )
    #     )
    #     if len(relational_products):
    #         rep["relational_products"] = relational_products
    #     else:
    #         rep["relational_products"] = []
    #     return rep
