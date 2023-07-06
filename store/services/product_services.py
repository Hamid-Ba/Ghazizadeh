from store import models

class ProductServices:
    """Service of Product"""

    def __init__(self) -> None:
        self.products = models.Product.objects.all()
    
    def get_available_products(self):
        """Return List Of Product With Available Count Greater Than 2"""
        return self.products.filter(count__gte=2)