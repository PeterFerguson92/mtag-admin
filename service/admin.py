import io
import xlsxwriter
from datetime import date
from django.contrib import admin
from .models import Attendance, ServicePlanning
from django.http import HttpResponse

# Register your models here.


@admin.action()
def export_to_xls(self, request, queryset):
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})
    time_format = workbook.add_format({'num_format': 'hh:mm'})
    time_format.set_align('center')
    bold = workbook.add_format({"bold": True})
    bold.set_align('center')
    normal_format = workbook.add_format()
    normal_format.set_align('center')

    for s in queryset:
        worksheet_name = f"{s.date.strftime('%d %m %Y')} planning"

        worksheet = workbook.add_worksheet(worksheet_name)
        
        worksheet.set_column(1, 2, 50)

        # Write the title for every column in bold
        worksheet.write("A1", "Item", bold)
        worksheet.write("B1", "Expected", bold)
        worksheet.write("C1", "Expected Start Time", bold)
        worksheet.write("D1", "Expected End Time", bold)
        worksheet.write("E1", "Actual", bold)
        worksheet.write("F1", "Actual Start Time", bold)
        worksheet.write("G1", "Actual End Time", bold)

        worksheet.write(1, 0, "date", normal_format)
        worksheet.write(1, 1, s.date.strftime("%d/%m/%Y"), normal_format)
        worksheet.write(1, 2, "-",normal_format)
        worksheet.write(1, 3, "-", normal_format)
        worksheet.write(1, 4, s.date.strftime("%d/%m/%Y"), normal_format)
        worksheet.write(1, 5, "-", normal_format)
        worksheet.write(1, 6, "-", normal_format)

        worksheet.write(2, 0, "MC", normal_format)
        worksheet.write(2, 1, s.expected_mc, normal_format)
        worksheet.write(2, 2, s.expected_mc_start_time, time_format)
        worksheet.write(2, 3, s.expected_mc_end_time, time_format)
        worksheet.write(2, 4, s.mc,normal_format)
        worksheet.write(2, 5, s.mc_start_time, time_format)
        worksheet.write(2, 6, s.mc_end_time, time_format)

        worksheet.write(3, 0, "Worship & Praises",normal_format)
        worksheet.write(3, 1, s.expected_worship_praise,normal_format)
        worksheet.write(3, 2, s.expected_worship_praise_start_time, time_format)
        worksheet.write(3, 3, s.expected_worship_praise_end_time, time_format)
        worksheet.write(3, 4, s.worship_praise, normal_format)
        worksheet.write(3, 5, s.worship_praise_start_time, time_format)
        worksheet.write(3, 6, s.worship_praise_end_time, time_format)
        
        worksheet.write(4, 0, "Bible Reading", normal_format)
        worksheet.write(4, 1, s.expected_bible_reading,normal_format)
        worksheet.write(4, 2, s.expected_bible_reading_start_time, time_format)
        worksheet.write(4, 3, s.expected_bible_reading_end_time, time_format)
        worksheet.write(4, 4, s.bible_reading, normal_format)
        worksheet.write(4, 5, s.bible_reading_start_time, time_format)
        worksheet.write(4, 6, s.bible_reading_end_time, time_format)
        
        worksheet.write(5, 0, "MTAG News", normal_format)
        worksheet.write(5, 1, s.expected_mtag_news, normal_format)
        worksheet.write(5, 2, s.expected_mtag_news_start_time, time_format)
        worksheet.write(5, 3, s.expected_mtag_news_end_time, time_format)
        worksheet.write(5, 4, s.mtag_news, normal_format)
        worksheet.write(5, 5, s.mtag_news_start_time, time_format)
        worksheet.write(5, 6, s.mtag_news_end_time, time_format)
        
        worksheet.write(6, 0, "Offering & Ministration", normal_format)
        worksheet.write(6, 1, s.expected_offering_ministration, normal_format)
        worksheet.write(6, 2, s.expected_offering_ministration_start_time, time_format)
        worksheet.write(6, 3, s.expected_offering_ministration_end_time, time_format)
        worksheet.write(6, 4, s.offering_ministration, normal_format)
        worksheet.write(6, 5, s.offering_ministration_start_time, time_format)
        worksheet.write(6, 6, s.offering_ministration_end_time, time_format)
        
        worksheet.write(7, 0, "Sermon", normal_format)
        worksheet.write(7, 1, s.expected_sermon, normal_format)
        worksheet.write(7, 2, s.expected_sermon_start_time, time_format)
        worksheet.write(7, 3, s.expected_sermon_end_time, time_format)
        worksheet.write(7, 4, s.sermon, normal_format)
        worksheet.write(7, 5, s.sermon_start_time, time_format)
        worksheet.write(7, 6, s.sermon_end_time, time_format)

        worksheet.autofit()

    workbook.close()

    output.seek(0)
    today = date.today()
    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
        "service_outline_" + today.strftime("%d/%m/%Y")
    )

    return response


export_to_xls.short_description = "Export to XLS"  # short description


@admin.register(ServicePlanning)
class EventAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "service_type",
        "date",
        "expected_mc",
        "expected_mc_start_time",
        "expected_mc_end_time",
        "mc",
        "mc_start_time",
        "mc_end_time",
        "expected_worship_praise",
        "expected_worship_praise_start_time",
        "expected_worship_praise_end_time",
        "worship_praise",
        "worship_praise_start_time",
        "worship_praise_end_time",
        "expected_bible_reading",
        "expected_bible_reading_start_time",
        "expected_bible_reading_end_time",
        "bible_reading",
        "bible_reading_start_time",
        "bible_reading_end_time",
        "expected_mtag_news",
        "expected_mtag_news_start_time",
        "expected_mtag_news_end_time",
        "mtag_news",
        "mtag_news_start_time",
        "mtag_news_end_time",
        "expected_offering_ministration",
        "expected_offering_ministration_start_time",
        "expected_offering_ministration_end_time",
        "offering_ministration",
        "offering_ministration_start_time",
        "offering_ministration_end_time",
        "expected_sermon",
        "expected_sermon_start_time",
        "expected_sermon_end_time",
        "sermon",
        "sermon_start_time",
        "sermon_end_time",
    )
    list_display = (
        "title",
        "date",
        "service_type",
        "created_at",
    )
    list_filter = ("date", "service_type",)
    actions = [export_to_xls]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    # search_fields = ("title__startswith",)
    fields = (
        "date",
        "number_of_mens",
        "number_of_women",
        "number_of_youth",
        "number_of_children",
        "total",
        "service_type",
    )
    list_display = (
        "date",
        "service_type",
        "created_at",
    )
    list_filter = ("date", "service_type",)