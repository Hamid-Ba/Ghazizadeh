from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from config import pagination

from car import serializers
from car.services import car_services

# Create your views here.

car_service = car_services.CarServices()


class CarViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Car View Set"""

    queryset = car_service.get_newest_cars()
    serializer_class = serializers.CarListSerializer
    pagination_class = pagination.StandardPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["brand"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.CarSerializer

        return self.serializer_class
