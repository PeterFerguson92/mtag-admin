import io
import xlsxwriter
from datetime import date
from .models import Member
from django.http import HttpResponse

def export_member_attendace():
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})
    
    time_format = workbook.add_format({'num_format': 'hh:mm'})
    time_format.set_align('center')
    bold = workbook.add_format({"bold": True})
    bold.set_align('center')
    normal_format = workbook.add_format()
    normal_format.set_align('center')

    mens_members = get_members_by_department("MEN")
    women_members = get_members_by_department("WOMEN")
    youth_members = get_members_by_department("YOUTH")
    children_members = get_members_by_department("CHILDREN")
    process_attendance_worksheet("MEN",workbook, mens_members, bold, normal_format)
    process_attendance_worksheet("WOMEN",workbook, women_members, bold, normal_format)
    process_attendance_worksheet("YOUTH",workbook, youth_members, bold, normal_format)
    process_attendance_worksheet("CHILDREN",workbook, children_members, bold, normal_format)

    workbook.close()

    output.seek(0)
    today = date.today()
    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment;" "filename={}.xlsx".format(
        "attendance_outline_" + today.strftime("%d/%m/%Y")
    )

    return response

def get_members_by_department(department):
    return Member.objects.filter(department=department)

def process_attendance_worksheet(worksheet_name, workbook, members, bold, normal_format):
    worksheet_name = worksheet_name
    worksheet = workbook.add_worksheet(worksheet_name)
    worksheet.write("A1", "DATE", bold)
    worksheet.write("A2", "FULL NAME", bold)
    worksheet.write("B2", "ATTENDANCE", bold)
    
    row = 2
    col = 0
    
    for s in members:
        worksheet.write(row, col, f"{s.name} {s.middle_name} {s.surname}", normal_format)
        row += 1
    worksheet.autofit()
    