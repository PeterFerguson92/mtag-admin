import io
import xlsxwriter
from datetime import date
from django.contrib import admin
from .models import ServicePlanning
from django.http import HttpResponse
# Register your models here.

@admin.action()
def export_to_xls(self, request, queryset):
        # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    
    for s in queryset:
        worksheet_name = f"{s.date.strftime('%d %m %Y')} planning"
        
        worksheet = workbook.add_worksheet(worksheet_name)
        bold = workbook.add_format({'bold': True})
        worksheet.set_column(1, 2, 50)

        # Write the title for every column in bold
        worksheet.write('A1', "Item", bold)
        worksheet.write('B1', "Expected", bold)
        worksheet.write('C1', "Actual", bold)
    
        worksheet.write(1, 0, "date")
        worksheet.write(1, 1, s.date.strftime('%d/%m/%Y'))
        worksheet.write(1, 2, s.date.strftime('%d/%m/%Y'))
        
        worksheet.write(2, 0, "MC")
        worksheet.write(2, 1, s.expected_mc)
        worksheet.write(2, 2, s.mc)
        
        worksheet.write(3, 0, "Worship & Praises")
        worksheet.write(3, 1, s.expected_worship_praise)
        worksheet.write(3, 2, s.worship_praise)
        
        worksheet.write(4, 0, "Bible Reading")
        worksheet.write(4, 1, s.expected_bible_reading)
        worksheet.write(4, 2, s.bible_reading)
        
        worksheet.write(5, 0, "MTAG News")
        worksheet.write(5, 1, s.expected_mtag_news)
        worksheet.write(5, 2, s.mtag_news)
        
        worksheet.write(6, 0, "Offering & Ministration")
        worksheet.write(6, 1, s.expected_offering_ministration)
        worksheet.write(6, 2, s.offering_ministration)
        
        worksheet.write(7, 0, "Sermon")
        worksheet.write(7, 1, s.expected_sermon)
        worksheet.write(7, 2, s.sermon)
        worksheet.autofit()
    
    workbook.close()

    output.seek(0)
    today = date.today()
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
    'service_outline_' + today.strftime('%d/%m/%Y'))
    
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
    actions = [export_to_xls]
