from django.contrib import admin

# Register your models here.
from .models import AboutUs, Homepage, Banner, Block

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
    
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "block_1_title",
        "block_1_text",
        "block_2_title",
        "block_2_text",
        "block_3_title",
        "block_3_text",
    )
    list_display = (
        "title",
        "created_at",
    )
    
@admin.register(AboutUs)
class BlockAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "homepage_display_header",
        "homepage_display_title",
        "homepage_display_text",
        "homepage_display_info_1",
        "homepage_display_info_1_text",
        "homepage_display_info_2",
        "homepage_display_info_2_text",
        "section_display_header",
        "section_display_title",
        "section_display_text",
        "section_display_info_1",
        "section_display_info_1_text",
        "section_display_info_2",
        "section_display_info_2_text",
    )
    list_display = (
        "title",
        "created_at",
    )
    
@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("banners","blocks")
    fields = (
        "title",
        "banners",
        "blocks",
        "aboutUs",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )