from rest_framework import (
    generics,
    mixins,
    viewsets,
    filters,
    authentication,
    permissions,
)
import requests
from django.conf import settings
from rest_framework import status
from django.shortcuts import redirect
from django.contrib.sites.models import Site
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from config import pagination
from store import models, serializers
from store.services import product_services, category_services
from store.filters import PriceRangeFilter

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO


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
    ordering_fields = ["created_date", "order_count", "price"]
    search_fields = ["title", "technical_number", "category__title"]


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


class CreateOrderApiView(generics.CreateAPIView):
    """Order Api View"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.CreateOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user).order_by("-registered_date")

    # def get_serializer_class(self):
    #     if self.action == "create":
    #         self.serializer_class = serializers.CreateOrderSerializer

    #     return self.serializer_class

    def create(self, request, *args, **kwargs):
        user = self.request.user
        request.data["user"] = user.id
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)

                if settings.DEBUG:
                    domain = Site.objects.filter(domain__contains="127").first()
                    req_url = f"http://{domain}/api/payment/place_order/{serializer.data['id']}/"
                    return Response(req_url, status=status.HTTP_201_CREATED)

                else:
                    domain = Site.objects.filter(domain__contains="api.ghazizadeh")

                    if domain.exists():
                        domain = domain.first()
                        http = "https"
                    else:
                        domain = "87.248.153.97:8000"
                        http = "http"
                    req_url = f"{http}://{domain}/api/payment/place_order/{serializer.data['id']}/"

                return redirect(req_url)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            error_message = str(e)  # Get the error message from the exception
            return Response(
                {"message": error_message}, status=status.HTTP_400_BAD_REQUEST
            )


class OrderViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Order View Set"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user).order_by("-registered_date")


class PaymentMethodViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Payment Method View Set"""

    queryset = models.PaymentMethod.objects.all()
    serializer_class = serializers.PaymentMethodSerializer


# def generate_pdf_invoice(request, order_id):
#     # Get the order and its associated items
#     order = models.Order.objects.get(pk=order_id)
#     items = order.items.all()

#     # Create a PDF document
#     buffer = BytesIO()
#     pdf = SimpleDocTemplate(buffer, pagesize=letter)
#     data = []

#     # Load the Persian font
#     font_path = "store/Vazir.ttf"
#     addMapping("Vazir", 0, 0, font_path)  # Use your desired font name

#     # Define styles with the Persian font
#     styles = getSampleStyleSheet()
#     style_heading = styles["Heading1"]
#     style_heading.fontName = "Vazir"

#     # Invoice header
#     data.append(["فاکتور", ""])
#     data.append(["شماره سفارش:", order.code])
#     data.append(["تاریخ ثبت سفارش:", order.registered_date.strftime("%Y/%m/%d %H:%M")])
#     data.append(["", ""])
#     data.append(["اطلاعات مشتری", ""])
#     data.append(["نام:", order.user.get_full_name()])
#     data.append(["تلفن:", order.phone])
#     data.append(["", ""])
#     data.append(["آیتم‌های سفارش", ""])
#     data.append(["نام محصول", "تعداد", "قیمت (تومان)"])
#     for item in items:
#         data.append([item.title, str(item.count), str(item.price)])

#     # Calculate total price
#     total_price = order.total_price
#     data.append(["", "", "مجموع قیمت:"])
#     data.append(["", "", str(total_price)])

#     # Create table
#     table = Table(data, colWidths=(200, 100, 100))
#     table.setStyle(
#         TableStyle(
#             [
#                 ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
#                 ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#                 ("FONTNAME", (0, 0), (-1, -1), "Vazir"),
#                 ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
#                 ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
#                 ("GRID", (0, 0), (-1, -1), 1, colors.black),
#             ]
#         )
#     )

#     # Add table to PDF
#     pdf.build([table])

#     # Return PDF as HTTP response
#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = f'attachment; filename="invoice_{order.id}.pdf"'
#     response.write(buffer.getvalue())
#     buffer.close()
#     return response


class FavoriteProductListCreateView(generics.ListCreateAPIView):
    queryset = models.FavoriteProduct.objects.all()
    serializer_class = serializers.FavoriteProductSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateFavoriteProductSerializer
        else:
            return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
