from rest_framework import generics, mixins, viewsets

from config import pagination
from store import models, serializers
from store.services import product_services

product_service = product_services.ProductServices()

class CategoryApiView(generics.ListAPIView):
    """Category Api View"""

    queryset = models.Category.objects.order_by("order")
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.StandardPagination


class ProductViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Prodcut View Set"""

    queryset = product_service.get_available_products().order_by("-created_date")
    serializer_class = serializers.ProductListSerializer
    pagination_class = pagination.StandardPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.ProductSerializer

        return self.serializer_class

class BestSellingProducts(generics.ListAPIView):
    """Best Selling Products"""
    
    queryset = product_service.get_available_products().order_by("-order_count")
    serializer_class = serializers.ProductListSerializer
    pagination_class = pagination.StandardPagination