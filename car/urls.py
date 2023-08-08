from rest_framework.routers import DefaultRouter
from django.urls import path, include

from car import views

app_name = "car"

router = DefaultRouter()
router.register("cars", views.CarViewSet)


urlpatterns = [
    path("", include(router.urls))
]
