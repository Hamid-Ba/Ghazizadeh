from rest_framework import generics

from config import pagination
from store import models, serializers


class CategoryApiView(generics.ListAPIView):
    """Category Api View"""

    queryset = models.Category.objects.order_by("order")
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.StandardPagination
