from django.contrib import admin

from car import models


# Register your models here.
class SpecificationInline(admin.TabularInline):
    model = models.Car_Specification
    extra = 1


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "brand"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    list_filter = ("brand",)
    inlines = [SpecificationInline]


admin.site.register(models.Car, CarAdmin)
