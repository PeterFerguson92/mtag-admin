import io
import decimal
import xlsxwriter
from datetime import date
from django.http import HttpResponse

def export_transaction_to_xls(queryset):
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