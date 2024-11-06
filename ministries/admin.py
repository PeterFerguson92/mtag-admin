from django.contrib import admin

from .models import Ministry

# Register your models here.
@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "short_description",
        "description",
        "cover_image_path",
        "index",
        "gallery_image_path_1",
        "gallery_image_path_2",
        "gallery_image_path_3",
    )
    list_display = ("name", "short_description")
    list_filter = (
        "name",
    )