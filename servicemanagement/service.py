import io
import xlsxwriter
import pandas as pd
from datetime import date
from .models import Absence, Member
from .models import Attendance
from django import forms
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import logging


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

def process_attendance_import(self, request):
    if request.method == "POST":
        print('HERE')
        xlsx_file = request.FILES["csv_upload"]
        
        if not xlsx_file.name.endswith('.xlsx'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        men_sheet = retrive_attendance_worksheet_data(xlsx_file, 'MEN')
        women_sheet = retrive_attendance_worksheet_data(xlsx_file, 'WOMEN')
        youth_sheet = retrive_attendance_worksheet_data(xlsx_file, 'YOUTH')
        children_sheet = retrive_attendance_worksheet_data(xlsx_file, 'CHILDREN')
        if (men_sheet["date"] == None or women_sheet["date"] == None
            or (youth_sheet["date"]== None) or children_sheet["date"] == None): 
            messages.warning(request, 'Please check the selected file, missing date on one or more worksheets')
            return HttpResponseRedirect(request.path_info)
        
        print('processing MEN')
        men_totals = process_attendance_worksheet(men_sheet)
        print('processing WOMEN')
        women_totals = process_attendance_worksheet(women_sheet)
        print('processing YOUTH')
        youth_totals = process_attendance_worksheet(youth_sheet)
        print('processing CHILDREN')
        children_totals = process_attendance_worksheet(children_sheet)
              
        total = men_totals["Total"] + women_totals["Total"] + youth_totals["Total"] + children_totals["Total"]
        Attendance.objects.create(date=men_totals['date'],
                                  number_of_mens=men_totals['present'],
                                  number_of_women=women_totals['present'],
                                  number_of_youth=youth_totals['present'],
                                  number_of_children=children_totals['present'],
                                  total=total)
            
        url = reverse('admin:index')
        return HttpResponseRedirect(url)
    
    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)

def retrive_attendance_worksheet_data(xlsx_file, worksheet_name):
    data = pd.read_excel(xlsx_file, sheet_name=worksheet_name,  header=None)
    rows = data.values.tolist()
    items = rows[2:]
    return { "date": get_date(rows[0][1]), "items": items}
    
def process_attendance_worksheet(data):
    date = data['date']
    items = data['items']
    total = 0
    total_absent = 0
    total_present = 0
    
    for p in items:
        total += 1
        members = Member.objects.filter(id=p[0])
        if(members.count() == 1):
            if(p[2] == 'P' or p[2] == 'p'):
                print(p[0])
                print('ATTENDED: ', date)
                logging.info("I am a breadcrumb")
                total_present+=1
                print('started updating last seen date for member with id', p[0])
                members[0].update(last_seen=date)
                print('updated last seen date for member with id', p[0])
            else:
                print(p[0])
                print('NOT ATTENDED: ', date)
                print('calculating absence for member with id', p[0])  
                delta = date - members[0].last_seen
                absentDays = delta.days
                print('number of absence days for member with id: ', absentDays)
                if(absentDays > 7):
                    print('creating absence for member with id', p[0])
                    Absence.objects.create(member=members[0], contact_phone_number=members[0].telephone, last_seen=members[0].last_seen)
                    print('created absence for member with id', p[0])
        results = { 
                "date": date,
                "Total": total,
                "absent": total_absent,
                "present": total_present
            }
    return results
  
def get_date(raw):
   if raw and 'pandas._libs.tslibs.timestamps.Timestamp' in str(type(raw)):
       return raw.date()
   else:
       return None

def export_member_attendace(user):
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})
    
    time_format = workbook.add_format({'num_format': 'hh:mm'})
    time_format.set_align('center')
    bold = workbook.add_format({"bold": True})
    bold.set_align('center')
    normal_format = workbook.add_format()
    normal_format.set_align('center')

    if(user == 'root'):
        mens_members = get_members_by_department("MEN")
        women_members = get_members_by_department("WOMEN")
        youth_members = get_members_by_department("YOUTH")
        children_members = get_members_by_department("CHILDREN")
        build_attendance_worksheet("MEN",workbook, mens_members, bold, normal_format)
        build_attendance_worksheet("WOMEN",workbook, women_members, bold, normal_format)
        build_attendance_worksheet("YOUTH",workbook, youth_members, bold, normal_format)
        build_attendance_worksheet("CHILDREN",workbook, children_members, bold, normal_format)
    
    if(user == 'men_dpt'):
        members = get_members_by_department("MEN")
        build_attendance_worksheet("MEN", workbook, members, bold, normal_format)
        
    if(user == 'women_dpt'):
        members = get_members_by_department("WOMEN")
        build_attendance_worksheet("WOMEN", workbook, members, bold, normal_format)
        
    if(user == 'children_dpt'):
        members = get_members_by_department("CHILDREN")
        build_attendance_worksheet("CHILDREN", workbook, members, bold, normal_format)
        
    if(user == 'youth_dpt'):
        members = get_members_by_department("YOUTH")
        build_attendance_worksheet("YOUTH", workbook, members, bold, normal_format)
        
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
    return Member.objects.filter(department=department, active=True)

def build_attendance_worksheet(worksheet_name, workbook, members, bold, normal_format):
    today = date.today()
    worksheet_name = worksheet_name
    worksheet = workbook.add_worksheet(worksheet_name)
    worksheet.write("A1", "DATE", bold)
    worksheet.write("A2", "MEMBER ID", bold)
    worksheet.write("B2", "FULL NAME", bold)
    worksheet.write("C2", "ATTENDANCE", bold)
    
    row = 2
    col = 0
    
    for s in members:
        worksheet.write(row, col, s.id, normal_format)
        worksheet.write(row, col+1, f"{s.name} {s.middle_name} {s.surname}", normal_format)
        row += 1
    worksheet.autofit()
    
    
def export_service_planning_to_xls(queryset):
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

def archive_members(queryset):
    print(queryset)
    queryset.update(archived=True)
    pass