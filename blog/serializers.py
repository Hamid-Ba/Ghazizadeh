"""
Blog Module Serializer
"""
from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from blog import models
from gallery import serializers as gallery_serializers


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""

    class Meta:
        model = models.Category
        fields = "__all__"


class SpecificationSerializer(serializers.ModelSerializer):
    """Specification Serializer"""

    class Meta:
        model = models.Specification
        fields = "__all__"


class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Blog Serializer"""

    tags = TagListSerializerField()
    category = CategorySerializer(many=False)
    specs = SpecificationSerializer(many=True)
    image = gallery_serializers.GallerySerializer(many=False)

    class Meta:
        model = models.Blog
        fields = "__all__"


class LatestBlogSerializer(serializers.ModelSerializer):
    """Latest Blog Serializer"""

    category = CategorySerializer(many=False)
    image = gallery_serializers.GallerySerializer(many=False)

    class Meta:
        model = models.Blog
        fields = ["title", "slug", "category", "image"]
