from django.contrib import admin

# Register your models here.
from .models import Weekly, Event, Monthly

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
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
    filter_horizontal = ("events",)
    fields = (
        "title",
        "month",
        "events",
    )
    list_display = (
        "title",
        "month",
        "created_at",
    )
    list_filter = ("month",)
