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


class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        """Meta Class"""

        model = models.Category
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["subs"] = []

        if instance.sub_categories.exists():
            rep["subs"] = instance.sub_categories.order_by("-order").values()

        return rep


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Comment
        fields = "__all__"
        read_only_fields = ["user","is_active"]

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
        fields = ["id","title", "price", "category", "brand", "gallery"]


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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        relational_products = (
            models.Product.objects.get_relational_products_by_category(
                instance.category.id
            )
        )
        if len(relational_products):
            rep["relational_products"] = relational_products
        else:
            rep["relational_products"] = []
        return rep
