from django.contrib import admin

# Register your models here.
from .models import Homepage, Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "text",
        "image",
        "image_position",
    )
    list_display = (
        "title",
        "text",
        "created_at",
    )
    
@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("banners",)
    fields = (
        "title",
        "banners",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )