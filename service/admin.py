import csv
from django.http import HttpResponse
from django.contrib import admin

# Register your models here.
from .models import ServicePlanning

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment;" "filename={}.csv".format(
        'service_outline_' + queryset[0].date.strftime('%d/%m/%Y')
    )
    writer = csv.writer(response)
    writer.writerow(
        [
            "Item",
            "Expected",
            "Actual",
        ]
    )

    writer.writerow(["date", queryset[0].date.strftime('%d/%m/%Y'), queryset[0].date.strftime('%d/%m/%Y')])
    writer.writerow(["MC", queryset[0].expected_mc, queryset[0].mc])
    writer.writerow(["Worship & Praises", queryset[0].expected_worship_praise, queryset[0].worship_praise])
    writer.writerow(["Bible Reading", queryset[0].expected_bible_reading, queryset[0].bible_reading])
    writer.writerow(["MTAG News", queryset[0].expected_mtag_news, queryset[0].mtag_news])
    writer.writerow(["Offering & Ministration", queryset[0].expected_offering_ministration, queryset[0].offering_ministration])
    writer.writerow(["Sermon", queryset[0].expected_sermon, queryset[0].sermon])

    return response

export_to_csv.short_description = "Export to CSV"  # short description


@admin.register(ServicePlanning)
class EventAdmin(admin.ModelAdmin):
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
    actions = [export_to_csv]
