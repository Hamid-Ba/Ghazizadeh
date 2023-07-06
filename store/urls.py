from rest_framework.routers import DefaultRouter
from django.urls import path, include

from store import views

app_name = "store"

router = DefaultRouter()
router.register("products", views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("best_selling_products", views.BestSellingProducts.as_view(), name="best_selling_products"),
    path("categories", views.CategoryApiView.as_view(), name="categories"),
]
