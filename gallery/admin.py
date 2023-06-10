from django.contrib import admin

from gallery import models
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    """Gallery Admin Model"""

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    sortable_by = ["title"]
    search_fields = ["title"]
    
admin.site.register(models.Gallery, GalleryAdmin)