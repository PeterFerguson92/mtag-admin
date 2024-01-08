from django.contrib import admin

# Register your models here.
from .models import Weekly, Event, Monthly

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "description", "day", "time", "date")
    list_display = (
        "title",
        "description",
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