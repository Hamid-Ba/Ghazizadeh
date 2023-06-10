"""
Blog Module Views
"""
from rest_framework import generics
from django.utils import timezone

from blog.pagination import BlogPagination
from blog import serializers, models

class BlogDetailView(generics.RetrieveAPIView):
    """Detail Of Blog View"""

    lookup_field = "slug"
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class BlogsView(generics.ListAPIView):
    """List Of Blogs View"""

    queryset = models.Blog.objects.all()
    pagination_class = BlogPagination
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        return self.queryset.filter(publish_date__lte=timezone.now()).order_by(
            "-publish_date"
        )

class LatestBlogsView(generics.ListAPIView):
    """List Of Latest Blogs View"""

    queryset = models.Blog.objects.all()
    serializer_class = serializers.LatestBlogSerializer

    def get_queryset(self):
        return self.queryset.filter(publish_date__lte=timezone.now()).order_by(
            "-publish_date"
        )[:3]
