from django.contrib import admin

from car import models

# Register your models here.
class SpecificationInline(admin.TabularInline):
    model = models.Car_Specification
    extra = 1


class CarAdmin(admin.ModelAdmin):
    inlines = [SpecificationInline]

admin.site.register(models.Car, CarAdmin)