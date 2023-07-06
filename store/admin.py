from django.contrib import admin

from store import models


class SpecificationInline(admin.TabularInline):
    model = models.Specifications
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    # list_display = ("title", "category", "publish_date")
    # list_filter = ("category", "tags")
    # search_fields = ("title", "short_desc", "desc")

    inlines = [SpecificationInline]

    # fieldsets = (
    #     (
    #         None,
    #         {
    #             "fields": ("title", "slug", "image", "short_desc", "desc"),
    #         },
    #     ),
    #     (
    #         "Image Details",
    #         {
    #             "fields": ("image_alt", "image_title"),
    #             "classes": ("collapse",),
    #         },
    #     ),
    #     (
    #         "Date",
    #         {
    #             "fields": ("publish_date",),
    #         },
    #     ),
    #     (
    #         "Tag and Category",
    #         {
    #             "fields": ("tags", "category"),
    #         },
    #     ),
    # )

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.prefetch_related("specs")

    #     return queryset


admin.site.register(models.Category)
admin.site.register(models.Product, ProductAdmin)
