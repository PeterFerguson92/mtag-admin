from django.contrib import admin

# Register your models here.
from .models import (
    AboutUs,
    Broadcast,
    Details,
    Homepage,
    Banner,
    Block,
    Leader,
    LeadershipBoard,
    Media,
    SocialMedia,
    Video,
)


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
class AboutUsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "homepage_display_header",
        "homepage_display_title",
        "homepage_display_text",
        "homepage_display_info_1",
        "homepage_display_info_1_text",
        "homepage_display_info_2",
        "homepage_display_info_2_text",
        "homepage_image",
        "section_display_header",
        "section_display_title",
        "section_display_text",
        "section_display_info_1",
        "section_display_info_1_text",
        "section_display_info_2",
        "section_display_info_2_text",
        "image_1",
        "image_2",
        "image_3",
        "image_4",
    )
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Details)
class DetailAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "info_text_1",
        "info_content_1",
        "info_text_2",
        "info_content_2",
        "address",
        "description"
    )
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "description", "date", "image", "url", "featured")
    list_display = (
        "title",
        "featured",
        "description",
        "created_at",
    )


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "subtitle",
        "link",
        "preview_image",
        "stream_title",
        "stream_subtitle",
        "stream_description",
    )
    list_display = (
        "title",
        "subtitle",
        "link",
        "created_at",
    )


@admin.register(SocialMedia)
class BroadcastAdmin(admin.ModelAdmin):
    fields = (
        "facebook_link",
        "tiktok_link",
    )
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("videos",)
    fields = (
        "title",
        "videos_header",
        "videos_title",
        "videos",
    )
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    search_fields = ("fullName__startswith",)
    fields = ("fullName", "role", "description", "phone", "address", "image")
    list_display = (
        "fullName",
        "role",
    )


@admin.register(LeadershipBoard)
class LeadershipBoardAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("leaders",)
    fields = (
        "title",
        "header",
        "section_title",
        "leaders",
    )
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("banners",)
    fields = (
        "title",
        "banners",
        "blocks",
        "aboutUs",
        "details",
        "media",
        "leadershipBoard",
        "banner_background_image",
        "leadership_board_background_image",
    )
    list_display = (
        "title",
        "banner_background_image",
        "leadership_board_background_image",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
