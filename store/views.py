from rest_framework import (
    generics,
    mixins,
    viewsets,
    filters,
    authentication,
    permissions,
)
from django_filters.rest_framework import DjangoFilterBackend


from config import pagination
from store import models, serializers
from store.services import product_services, category_services
from store.filters import PriceRangeFilter

product_service = product_services.ProductServices()
category_service = category_services.CategoryServices()


class CategoryApiView(generics.ListAPIView):
    """Category Api View"""

    queryset = models.Category.objects.order_by("order")
    serializer_class = serializers.CategorySerializer
    # pagination_class = pagination.StandardPagination


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """Category Api View"""

    queryset = category_service.get_parent_cats()
    serializer_class = serializers.ParentCategorySerializer
    # pagination_class = pagination.StandardPagination


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


class BestSellingProductsAPI(generics.ListAPIView):
    """Best Selling Products"""

    queryset = product_service.get_available_products().order_by("-order_count")
    serializer_class = serializers.ProductListSerializer
    pagination_class = pagination.StandardPagination


class SearchProductsAPI(generics.ListAPIView):
    """Search Products API"""

    queryset = product_service.get_available_products().order_by("-created_date")
    serializer_class = serializers.ProductListSerializer
    pagination_class = pagination.StandardPagination
    filter_class = PriceRangeFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["brand", "category"]
    search_fields = ["title", "category__title"]
    ordering_fields = ["created_date", "order_count", "price"]


# class ProductsCommentsApi(generics.ListAPIView):
#     queryset = models.Comment.objects.filter(is_active=True)
#     serializer_class = serializers.CommentSerializer

#     def list(self, request, product_id, *args, **kwargs):
#         self.queryset = self.queryset.filter(product__pk=product_id, is_active=True)
#         return super().list(request, *args, **kwargs)


class CreateCommentApi(generics.CreateAPIView):
    """Create Comment API"""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
