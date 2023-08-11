from django.contrib import admin
from django import forms
from store import models


class SubCategoryInline(admin.StackedInline):
    model = models.Category
    extra = 0
    verbose_name_plural = "Sub Categories"


class AddCategoryForm(forms.ModelForm):
    class Meta:
        models = models.Category

    def clean(self):
        is_cart = self.cleaned_data.get("is_cart")

        if is_cart:
            if models.Category.objects.filter(is_cart=True).count() < 4:
                return self.cleaned_data
            else:
                self.add_error(
                    "is_cart", "تعداد دسته بندی های کارتی بیشتر از ۴ مورد مجاز نمی باشد"
                )
                raise forms.ValidationError(
                    "تعداد دسته بندی های کارتی بیشتر از ۴ مورد مجاز نمی باشد"
                )


class CategoryAdmin(admin.ModelAdmin):
    form = AddCategoryForm
    list_display = ("title", "order", "parent")
    list_filter = ("parent",)
    search_fields = ("title",)

    inlines = [SubCategoryInline]

    fieldsets = (
        (None, {"fields": ("title", "logo", "order", "is_cart")}),
        (
            "Parent",
            {
                "fields": ("parent",),
                "description": "Select a category to make it a parent category",
            },
        ),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("sub_categories")

        return queryset


class SpecificationInline(admin.TabularInline):
    model = models.Specifications
    extra = 1


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "is_active", "create_data")
    list_display_links = ("id", "full_name")
    list_editable = ("is_active",)


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


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Comment, CommentAdmin)
