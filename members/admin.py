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
    search_fields = ("name__startswith",)
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


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("type__startswith",)
    fields = (
        "amount",
        "type",
        "member",
        "date",
        "month",
        "service_type",
    )
    list_display = ("type", "member_name", "date", "month")
    list_filter = ("type", "date", "member", "month")
    actions = ["export_to_xls"]

    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
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
        worksheet.write('B1', 'Type', bold)
        worksheet.write('C1', 'Service type', bold)
        worksheet.write('D1', 'Month', bold)
        worksheet.write('E1', 'Date', bold)
        worksheet.write('F1', 'Amount', bold)
        
        # Start from the first cell. Rows and columns are zero indexed.
        row = 1
        col = 0

        # Iterate over the data and write it out row by row.
        for s in queryset:
            total_amount = total_amount + s.amount
            worksheet.write(row, col, f"{s.member.name} {s.member.middle_name} {s.member.surname}", normal_format)
            worksheet.write(row, col + 1,  s.type, normal_format)
            worksheet.write(row, col + 2, s.service_type, normal_format)
            worksheet.write(row, col + 3, s.month, normal_format)
            worksheet.write(row, col + 4, s.date.strftime("%d/%m/%Y"), normal_format)
            worksheet.write(row, col + 5, s.amount, normal_format)
            row += 1

        worksheet.write(row+1, 0, 'Total Amount', bold)
        worksheet.write(row+1, col + 5, total_amount, bold)
        worksheet.autofit()
        workbook.close()

        output.seek(0)
        today = date.today()
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
        'transactions_outline_' + today.strftime('%d/%m/%Y'))
        
        return response

    export_to_xls.short_description = "Export to XLS"  # short description