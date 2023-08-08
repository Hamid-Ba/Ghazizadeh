from rest_framework import mixins, viewsets

import pagination

from car import serializers
from car.services import car_services
# Create your views here.

car_service = car_services.CarServices()

class CarViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Car View Set"""
    queryset = car_service.get_newest_cars()
    serializer_class = serializers.CarListSerializer
    pagination_class = pagination.StandardPagination
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            self.serializer_class = serializers.CarSerializer

        return self.serializer_class