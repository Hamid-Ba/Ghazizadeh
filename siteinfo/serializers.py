"""
site info modules serializers
"""
from siteinfo.models import AboutUs, ContactUs

from rest_framework import serializers


class AboutUsSerializer(serializers.ModelSerializer):
    """About Us Serializer"""

    class Meta:
        """Meta Class"""

        model = AboutUs
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    """Contact Us Serializer"""

    class Meta:
        """Meta Class"""

        model = ContactUs
        fields = "__all__"
