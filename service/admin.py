from django.contrib import admin

# Register your models here.
from .models import ServicePlanning

@admin.register(ServicePlanning)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "service_type", "date","expected_mc" ,"mc", "expected_worship_praise", "worship_praise", "expected_bible_reading","bible_reading",
              "expected_mtag_news", "mtag_news","expected_offering_ministration", "offering_ministration","expected_sermon", "sermon")
    list_display = (
        "title",
        "service_type",
        "date",
        "created_at",
    )