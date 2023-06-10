"""
site info modules views
"""

from rest_framework import generics
from rest_framework.response import Response

from siteinfo import models, serializers


class AboutUsView(generics.RetrieveAPIView):
    """About Us View"""

    serializer_class = serializers.AboutUsSerializer
    queryset = models.AboutUs.objects.all()

    def get(self, request):
        about_us = models.AboutUs.objects.first()
        serializer = serializers.AboutUsSerializer(about_us)
        return Response(serializer.data)


class ContactUsView(generics.ListAPIView):
    """Contact Us View"""

    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
