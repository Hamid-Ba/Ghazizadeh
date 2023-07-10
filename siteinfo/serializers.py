"""
site info modules serializers
"""
from siteinfo import models

from rest_framework import serializers


class AboutUsSerializer(serializers.ModelSerializer):
    """About Us Serializer"""

    class Meta:
        """Meta Class"""

        model = models.AboutUs
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    """Contact Us Serializer"""

    class Meta:
        """Meta Class"""

        model = models.ContactUs
        fields = "__all__"


class HomeHeaderSerializer(serializers.ModelSerializer):
    """Home Header Seraializer"""

    class Meta:
        """Meta Class"""

        model = models.HomeHeader
        fields = "__all__"


class FooterSerializer(serializers.ModelSerializer):
    """Footer Seraializer"""

    class Meta:
        """Meta Class"""

        model = models.Footer
        fields = "__all__"


class SliderAndBannerSerializer(serializers.ModelSerializer):
    """SliderAndBanner Seraializer"""

    class Meta:
        """Meta Class"""

        model = models.SliderAndBanner
        fields = "__all__"
