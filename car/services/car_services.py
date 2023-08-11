from car import models


class CarServices:
    """Service of Car"""

    def __init__(self) -> None:
        self.cars = models.Car.objects.all()

    def get_newest_cars(self):
        return self.cars.order_by("-id")
