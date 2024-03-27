from django.contrib import admin

# Register your models here.
from .models import SocialEvent, Weekly, Event, Monthly, Program

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "short_description",
        "description",
        "day",
        "start_time",
        "end_time",
        "location",
        "cover_image_path",
    )
    list_display = (
        "title",
        "short_description",
        "created_at",
    )
    
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "short_description",
        "description",
        "speaker",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "location",
        "cover_image_path",
    )
    list_display = (
        "title",
        "short_description",
        "created_at",
    )

@admin.register(Weekly)
class WeeklyAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("events",)
    fields = (
        "title",
        "events",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(Monthly)
class MonthlyAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("programs",)
    fields = (
        "title",
        "month",
        "programs",
    )
    list_display = (
        "title",
        "month",
        "created_at",
    )
    list_filter = ("month",)

@admin.register(SocialEvent)
class SocialEventAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "short_description",
        "description",
        "day",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "location",
        "cover_image_path",
        "gallery_image_path_1",
        "gallery_image_path_2",
    )
    list_display = (
        "title",
        "short_description",
        "created_at",
    )