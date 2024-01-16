import csv
from http.client import HTTPResponse
from django.contrib import admin
from import_export.admin import ExportActionMixin

# Register your models here.
from .models import ServicePlanning


class ExportCsvMixin:
    def export_to_csv(self, request, queryset):
        qs = ServicePlanning.objects.all()
        print(qs)

        # Create the HttpResponse object with the appropriate CSV header.
        response = HTTPResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="export_file.csv"'

        wr
        writer = csv.writer(response)

        for rule in qs:
            writer.writerow([rule.service_type])
            for c in rule:
                writer.writerow([c.sermon])

        return response

    export_to_csv.short_description = "Export Selected"


@admin.register(ServicePlanning)
class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "service_type",
        "date",
        "expected_mc",
        "mc",
        "expected_worship_praise",
        "worship_praise",
        "expected_bible_reading",
        "bible_reading",
        "expected_mtag_news",
        "mtag_news",
        "expected_offering_ministration",
        "offering_ministration",
        "expected_sermon",
        "sermon",
    )
    list_display = (
        "title",
        "service_type",
        "date",
        "created_at",
    )
    actions = ["export_to_csv"]

