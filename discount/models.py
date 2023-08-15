from datetime import datetime

from django.db import models

class DiscountCode(models.Model):
    """Discount Code Model"""
    
    code = models.CharField(max_length=25, null=False, blank=False)
    percentage = models.IntegerField(default=0, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    count = models.IntegerField(default=0, null=False, blank=False)
    reason = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.id}-{self.code}"
    
    def code_used(self):
        self.count -= 1
        self.save()
        
    def is_code_still_work(self):
        return (self.start_date <= datetime.now() and datetime.now <= self.end_date and self.count > 0)