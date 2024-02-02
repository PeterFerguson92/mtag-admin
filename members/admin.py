import io
import decimal
import xlsxwriter
from datetime import date
from django.contrib import admin
from django.http import HttpResponse
from daterange.filters import DateRangeFilter
from .models import SOURCE, BankAccount, Member, Transaction
from django.core.exceptions import ObjectDoesNotExist
from .service import export_member_attendace
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MemberResource(resources.ModelResource):

    class Meta:
        model = Member
        
@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin ):
    search_fields = ("name","surname", "postcode")
    fields = (
        "name",
        "middle_name",
        "surname",
        "telephone",
        "postcode",
        "house_number",
        "address",
        "date_of_birth",
        "age",
        "sex",
        "department",
        "member_type",
        "membership_start",
        "origin",
    )
    list_display = (
        "name",
        "middle_name",
        "surname",
        "department",
        "postcode",
        "house_number",
        "origin",
        "created_at",
    )
    list_filter = (
        "name",
        "surname",
        "postcode",
        "house_number",
        "sex",
        "department",
        "member_type",
        "membership_start",
        "origin",
        "created_at",
    )
    search_fields = ['name']
    actions = ["export_attendace_to_xls"]
    resource_classes = [MemberResource]
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results
    
    @admin.action()
    def export_attendace_to_xls(self, request, queryset):
        response = export_member_attendace()
        return response

    export_attendace_to_xls.short_description = "Export Attendance to XLS"  # short description
    

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("member__name","member__surname","member__postcode", "source")
    fields = (
        "amount",
        "type",
        "message",
        "member",
        "source",
        "date",
        "month",
        "service_type",
    )
    list_display = ("type", "member_name", "member_postcode_address","date", "month", "source")
    list_filter = ("type", "date", "member", "source", "month", ("date", DateRangeFilter))
    autocomplete_fields = ['member']
    change_list_template = "admin/daterange/change_list.html"
    actions = ["export_to_xls"]
    
    class Media:
        css = {"all": ("admin/css/forms.css", "css/admin/daterange.css")}
        js = ("admin/js/calendar.js", "js/admin/DateRangeShortcuts.js")

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.source == 'WEBSITE':
            return ["message"]
        return []
    
    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"
    
    def member_postcode_address(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            if(instance.member.postcode and instance.member.house_number):
                return f"{instance.member.postcode} - {instance.member.house_number}"
            else: 
                return ''
        except ObjectDoesNotExist:
            return "ERROR!!"

    @admin.action()
    def export_to_xls(self, request, queryset):
         # Create a workbook and add a worksheet.
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Transactions')
      
        bold = workbook.add_format({"bold": True})
        bold.set_align('center')
        normal_format = workbook.add_format()
        normal_format.set_align('center')
        total_amount = decimal.Decimal(0.00)

        # Write the title for every column in bold
        worksheet.write('A1', 'Full Name', bold)
        # worksheet.write('B1', 'Member Type', bold)
        worksheet.write('B1', 'Postcode', bold)
        worksheet.write('C1', 'House Number', bold)
        worksheet.write('D1', 'Source', bold)
        worksheet.write('E1', 'Type', bold)
        worksheet.write('F1', 'Service type', bold)
        worksheet.write('G1', 'Month', bold)
        worksheet.write('H1', 'Date', bold)
        worksheet.write('I1', 'Amount', bold)
        
        # Start from the first cell. Rows and columns are zero indexed.
        row = 1
        col = 0

        # Iterate over the data and write it out row by row.
        for s in queryset:
            total_amount = total_amount + s.amount
            worksheet.write(row, col, f"{s.member.name} {s.member.middle_name} {s.member.surname}", normal_format)
            if s.member.postcode :
                worksheet.write(row, col + 1, f"{s.member.postcode}", normal_format)
            else:
                worksheet.write(row, col + 1, "")
            if s.member.house_number:
                worksheet.write(row, col + 2, f"{s.member.house_number}", normal_format)
            else:
                worksheet.write(row, col + 2, "")
            worksheet.write(row, col + 3, s.source, normal_format)
            worksheet.write(row, col + 4, s.type, normal_format)
            worksheet.write(row, col + 5, s.service_type, normal_format)
            worksheet.write(row, col + 6, s.month, normal_format)
            worksheet.write(row, col + 7, s.date.strftime("%d/%m/%Y"), normal_format)
            worksheet.write(row, col + 8, s.amount, normal_format)
            row += 1

        worksheet.write(row+1, 0, 'Total Amount', bold)
        worksheet.write(row+1, col + 8, total_amount, bold)
        worksheet.autofit()
        workbook.close()

        output.seek(0)
        today = date.today()
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
        'transactions_outline_' + today.strftime('%d/%m/%Y'))
        
        return response

    export_to_xls.short_description = "Export to XLS"  # short description
    
    
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "account_holder_name",
        "account_number",
        "sort_code",
        "iban",
        "swift_bic",
        "visible",
    )
    list_display = (
        "name",
        "account_holder_name",
        "visible",
    )