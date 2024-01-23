import io
import decimal
import xlsxwriter
from datetime import date
from django.contrib import admin
from django.http import HttpResponse
from .models import Member, Transaction
from django.core.exceptions import ObjectDoesNotExist

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
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
        "member_type",
        "postcode",
        "house_number",
        "origin",
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
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("member__name","member__surname","member__postcode")
    fields = (
        "amount",
        "type",
        "member",
        "date",
        "month",
        "service_type",
    )
    list_display = ("type", "member_name", "member_postcode_address","date", "month")
    list_filter = ("type", "date", "member", "month",)
    autocomplete_fields = ['member']

    actions = ["export_to_xls"]

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
        worksheet.write('B1', 'Postcode', bold)
        worksheet.write('C1', 'House Number', bold)
        worksheet.write('D1', 'Type', bold)
        worksheet.write('E1', 'Service type', bold)
        worksheet.write('F1', 'Month', bold)
        worksheet.write('G1', 'Date', bold)
        worksheet.write('H1', 'Amount', bold)
        
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
            worksheet.write(row, col + 3, s.type, normal_format)
            worksheet.write(row, col + 4, s.service_type, normal_format)
            worksheet.write(row, col + 5, s.month, normal_format)
            worksheet.write(row, col + 6, s.date.strftime("%d/%m/%Y"), normal_format)
            worksheet.write(row, col + 7, s.amount, normal_format)
            row += 1

        worksheet.write(row+1, 0, 'Total Amount', bold)
        worksheet.write(row+1, col + 7, total_amount, bold)
        worksheet.autofit()
        workbook.close()

        output.seek(0)
        today = date.today()
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
        'transactions_outline_' + today.strftime('%d/%m/%Y'))
        
        return response

    export_to_xls.short_description = "Export to XLS"  # short description