from django.urls import path
from store import views

app_name = "store"

urlpatterns = [path("categories", views.CategoryApiView.as_view(), name="categories")]
