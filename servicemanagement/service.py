import io
from constants import EXCEL_1_SERVICE_INFO, EXCEL_2_SERVICE_INFO, EXCEL_SERVICES
from finance import service
import xlsxwriter
import pandas as pd
from datetime import date, datetime
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
        print("HERE")
        xlsx_file = request.FILES["csv_upload"]

        if not xlsx_file.name.endswith(".xlsx"):
            messages.warning(request, "The wrong file type was uploaded")
            return HttpResponseRedirect(request.path_info)
        men_sheet = retrive_attendance_worksheet_data(xlsx_file, "MEN")
        women_sheet = retrive_attendance_worksheet_data(xlsx_file, "WOMEN")
        youth_sheet = retrive_attendance_worksheet_data(xlsx_file, "YOUTH")
        children_sheet = retrive_attendance_worksheet_data(xlsx_file, "CHILDREN")
        if (
            men_sheet["date"] == None
            or women_sheet["date"] == None
            or (youth_sheet["date"] == None)
            or children_sheet["date"] == None
        ):
            messages.warning(
                request,
                "Please check the selected file, missing date on one or more worksheets",
            )
            return HttpResponseRedirect(request.path_info)

        print("--------------------------------------")
        print("Processing MEN")
        men_totals = process_attendance_worksheet(men_sheet)
        # print(men_totals)
        print("--------------------------------------")

        # print("processing WOMEN")
        # women_totals = process_attendance_worksheet(women_sheet)
        # print("--------------------------------------")
        # print("processing YOUTH")
        # youth_totals = process_attendance_worksheet(youth_sheet)
        # print("--------------------------------------")
        # print("processing CHILDREN")
        # children_totals = process_attendance_worksheet(children_sheet)

        # total = (
        #     men_totals["present"]
        #     + women_totals["present"]
        #     + youth_totals["present"]
        #     + children_totals["present"]
        # )
        # Attendance.objects.create(
        #     date=men_totals["date"],
        #     number_of_mens=men_totals["present"],
        #     number_of_women=women_totals["present"],
        #     number_of_youth=youth_totals["present"],
        #     number_of_children=children_totals["present"],
        #     total=total,
        # )

        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def process_men_attendance_import(self, request):
    print("--------------------------------------")

    attendance_type = "MEN"
    if request.method == "POST":
        xlsx_file = request.FILES["csv_upload"]

        if not xlsx_file.name.endswith(".xlsx"):
            messages.warning(request, "The wrong file type was uploaded")
            return HttpResponseRedirect(request.path_info)

        if check_sheet_present(xlsx_file, attendance_type) == False:
            messages.warning(
                request, "Content of sheet not valid, missing " + attendance_type
            )
            return HttpResponseRedirect(request.path_info)

        sheet = retrive_attendance_worksheet_data(xlsx_file, attendance_type)

        if sheet["date"] == None:
            messages.warning(
                request,
                "Please check the selected file, missing date on one or more worksheets",
            )
            return HttpResponseRedirect(request.path_info)

        print("processing: " + attendance_type)
        result = process_attendance_worksheet(sheet)
        # totals = []
        # print(result)
        # # payload = {
        # #     "date": result["date"],
        # #     "number_of_mens": result["present"],
        # #     "total": result["present"],
        # # }
        for service in EXCEL_SERVICES:
            print("processing results for: " + service["description"])
            processed_result = process_service_results(result, service["description"])
            payload = {
                "date": result["date"],
                "number_of_mens": processed_result["total"],
                "total": processed_result["total"],
            }
            create_or_update_attendance(processed_result['date'], payload)
            
        
       
        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def process_women_attendance_import(self, request):
    attendance_type = "WOMEN"

    if request.method == "POST":
        xlsx_file = request.FILES["csv_upload"]

        if not xlsx_file.name.endswith(".xlsx"):
            messages.warning(request, "The wrong file type was uploaded")
            return HttpResponseRedirect(request.path_info)

        if check_sheet_present(xlsx_file, attendance_type) == False:
            messages.warning(
                request, "Content of sheet not valid, missing " + attendance_type
            )
            return HttpResponseRedirect(request.path_info)

        sheet = retrive_attendance_worksheet_data(xlsx_file, attendance_type)

        if sheet["date"] == None:
            messages.warning(
                request,
                "Please check the selected file, missing date on one or more worksheets",
            )
            return HttpResponseRedirect(request.path_info)

        print("processing: " + attendance_type)
        result = process_attendance_worksheet(sheet)
        payload = {
            "date": result["date"],
            "number_of_women": result["present"],
            "total": result["present"],
        }

        create_or_update_attendance(result["date"], payload)

        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def process_youth_attendance_import(self, request):
    attendance_type = "YOUTH"

    if request.method == "POST":

        xlsx_file = request.FILES["csv_upload"]

        if not xlsx_file.name.endswith(".xlsx"):
            messages.warning(request, "The wrong file type was uploaded")
            return HttpResponseRedirect(request.path_info)

        if check_sheet_present(xlsx_file, attendance_type) == False:
            messages.warning(
                request, "Content of sheet not valid, missing " + attendance_type
            )
            return HttpResponseRedirect(request.path_info)

        sheet = retrive_attendance_worksheet_data(xlsx_file, attendance_type)

        if sheet["date"] == None:
            messages.warning(
                request,
                "Please check the selected file, missing date on one or more worksheets",
            )
            return HttpResponseRedirect(request.path_info)

        print("processing: " + attendance_type)
        result = process_attendance_worksheet(sheet)
        payload = {
            "date": result["date"],
            "number_of_youth": result["present"],
            "total": result["present"],
        }

        create_or_update_attendance(result["date"], payload)

        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def process_children_attendance_import(self, request):
    attendance_type = "CHILDREN"
    if request.method == "POST":

        xlsx_file = request.FILES["csv_upload"]

        if not xlsx_file.name.endswith(".xlsx"):
            messages.warning(request, "The wrong file type was uploaded")
            return HttpResponseRedirect(request.path_info)

        if check_sheet_present(xlsx_file, attendance_type) == False:
            messages.warning(
                request, "Content of sheet not valid, missing " + attendance_type
            )
            return HttpResponseRedirect(request.path_info)

        sheet = retrive_attendance_worksheet_data(xlsx_file, attendance_type)

        if sheet["date"] == None:
            messages.warning(
                request,
                "Please check the selected file, missing date on one or more worksheets",
            )
            return HttpResponseRedirect(request.path_info)

        print("processing: " + attendance_type)
        result = process_attendance_worksheet(sheet)
        payload = {
            "date": result["date"],
            "number_of_children": result["present"],
            "total": result["present"],
        }

        create_or_update_attendance(result["date"], payload)

        url = reverse("admin:index")
        return HttpResponseRedirect(url)

    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def check_sheet_present(xlsx_file, type):
    xl = pd.ExcelFile(xlsx_file)
    return type in xl.sheet_names

def process_service_results(results, service_type):
    total = 0
    for result in results:
        if result["service_type"] == service_type and result["is_present"]:
            total = total + 1

    return {'total': total, 'service_type': service_type, 'date':  result["date"]}

def create_or_update_attendance(date, payload):
    attendanceList = Attendance.objects.filter(date=date)
    if attendanceList.count() == 0:
        Attendance.objects.create(**payload)
    else:
        attendanceList.update(**payload)
        attendanceList[0].save()


def retrive_attendance_worksheet_data(xlsx_file, worksheet_name):
    data = pd.read_excel(xlsx_file, sheet_name=worksheet_name, header=None)
    rows = data.values.tolist()
    items = rows[2:]
    return {"date": get_date(rows[0][1]), "items": items}


def process_attendance_worksheet(data):
    export_date = data["date"]
    members_info = data["items"]
    total = 0
    services_result = []

    for member_row in members_info:
        total += 1
        members = Member.objects.filter(id=member_row[0])
        if members.count() == 1:
            # print("*******************************************")
            # print("Member in analysis: " + member_row[1])
            attendance = []
            for service in EXCEL_SERVICES:
                print("Processing service: " + service["description"])
                is_present = process_service(
                    member_row,
                    service["index"],
                    members,
                    export_date,
                )
                # print("ATTENDED " + service["description"] + ": " + str(is_present))
                attendance.append(
                    {
                        "service_type": service["description"],
                        "is_present": is_present,
                        "date": export_date,
                    }
                )
            is_member_absent = not any(obj['is_present'] == True for obj in attendance)   
            print(is_member_absent)             
            if(is_member_absent):
                print(members)
                create_member_absence(export_date, members)
            services_result.append({'name': member_row[1], 'attendance': attendance})


    return services_result


def is_member_present(member_row, service_index):
    return member_row[service_index] in ("p", "P")


def process_service(
    member_row,
    service_index,
    member_data,
    export_date,
):
    is_present = False
    if is_member_present(member_row, service_index):
        is_present = True
        member_data.update(last_seen=export_date)
    else:
        is_present = False
    return is_present

def create_member_absence(export_date, member_data):
    print('Creating absence for :')
    print(member_data)
    print(member_data[0].last_seen)
    delta = export_date - member_data[0].last_seen
    absentDays = delta.days
    print("number of absence days for member : ", absentDays)
    if absentDays > 7:
    # print("creating absence for member with id", member_row[0])
        Absence.objects.create(
            member=member_data[0],
            contact_phone_number=member_data[0].telephone,
            last_seen=member_data[0].last_seen,
        )


def get_date(raw):
    if raw:
        return datetime.strptime(raw, "%d-%m-%Y").date()
    else:
        return None


def export_member_attendace(user):
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})

    time_format = workbook.add_format({"num_format": "hh:mm"})
    time_format.set_align("center")
    bold = workbook.add_format({"bold": True})
    bold.set_align("center")
    normal_format = workbook.add_format()
    normal_format.set_align("center")

    if user == "root":
        mens_members = get_members_by_department("MEN")
        women_members = get_members_by_department("WOMEN")
        youth_members = get_members_by_department("YOUTH")
        children_members = get_members_by_department("CHILDREN")
        build_attendance_worksheet("MEN", workbook, mens_members, bold, normal_format)
        build_attendance_worksheet(
            "WOMEN", workbook, women_members, bold, normal_format
        )
        build_attendance_worksheet(
            "YOUTH", workbook, youth_members, bold, normal_format
        )
        build_attendance_worksheet(
            "CHILDREN", workbook, children_members, bold, normal_format
        )

    if user == "men_dpt":
        members = get_members_by_department("MEN")
        build_attendance_worksheet("MEN", workbook, members, bold, normal_format)

    if user == "women_dpt":
        members = get_members_by_department("WOMEN")
        build_attendance_worksheet("WOMEN", workbook, members, bold, normal_format)

    if user == "children_dpt":
        members = get_members_by_department("CHILDREN")
        build_attendance_worksheet("CHILDREN", workbook, members, bold, normal_format)

    if user == "youth_dpt":
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
        "attendance_outline_" + user + "_" + today.strftime("%d/%m/%Y")
    )

    return response


def get_members_by_department(department):
    return Member.objects.filter(department=department, active=True)


def build_attendance_worksheet(worksheet_name, workbook, members, bold, normal_format):
    today = date.today()
    format1 = workbook.add_format()
    format1.set_num_format("dd-mm-yyyy")
    format1.set_align("center")

    worksheet = workbook.add_worksheet(worksheet_name)
    worksheet.write("A1", "DATE", bold)
    worksheet.write("B1", today.strftime("%d-%m-%Y"), format1)
    worksheet.write("A2", "MEMBER ID", bold)
    worksheet.write("B2", "FULL NAME", bold)
    worksheet.write("C2", "ATTENDED 1 SERVICE ", bold)
    worksheet.write("D2", "ATTENDED 2 SERVICE ", bold)
    worksheet.write("E2", "ATTENDED 3 SERVICE ", bold)
    worksheet.write("F2", "ATTENDED JOINT SERVICE ", bold)

    row = 2
    col = 0

    for s in members:
        worksheet.write(row, col, s.id, normal_format)
        worksheet.write(
            row, col + 1, f"{s.name} {s.middle_name} {s.surname}", normal_format
        )
        row += 1
    worksheet.autofit()


def export_service_planning_to_xls(queryset):
    # Create a workbook and add a worksheet.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})
    time_format = workbook.add_format({"num_format": "hh:mm"})
    time_format.set_align("center")
    bold = workbook.add_format({"bold": True})
    bold.set_align("center")
    normal_format = workbook.add_format()
    normal_format.set_align("center")

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
        worksheet.write(1, 2, "-", normal_format)
        worksheet.write(1, 3, "-", normal_format)
        worksheet.write(1, 4, s.date.strftime("%d/%m/%Y"), normal_format)
        worksheet.write(1, 5, "-", normal_format)
        worksheet.write(1, 6, "-", normal_format)

        worksheet.write(2, 0, "MC", normal_format)
        worksheet.write(2, 1, s.expected_mc, normal_format)
        worksheet.write(2, 2, s.expected_mc_start_time, time_format)
        worksheet.write(2, 3, s.expected_mc_end_time, time_format)
        worksheet.write(2, 4, s.mc, normal_format)
        worksheet.write(2, 5, s.mc_start_time, time_format)
        worksheet.write(2, 6, s.mc_end_time, time_format)

        worksheet.write(3, 0, "Worship & Praises", normal_format)
        worksheet.write(3, 1, s.expected_worship_praise, normal_format)
        worksheet.write(3, 2, s.expected_worship_praise_start_time, time_format)
        worksheet.write(3, 3, s.expected_worship_praise_end_time, time_format)
        worksheet.write(3, 4, s.worship_praise, normal_format)
        worksheet.write(3, 5, s.worship_praise_start_time, time_format)
        worksheet.write(3, 6, s.worship_praise_end_time, time_format)

        worksheet.write(4, 0, "Bible Reading", normal_format)
        worksheet.write(4, 1, s.expected_bible_reading, normal_format)
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
    queryset.update(archived=True)
    pass
