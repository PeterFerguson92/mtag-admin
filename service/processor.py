import datetime
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import xlrd
from dateutil.parser import parse
import time

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

def process_attendance_import(self, request):
    if request.method == "POST":
        print('HERE')
        xlsx_file = request.FILES["csv_upload"]
        
        if not xlsx_file.name.endswith('.xlsx'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        print('processing MEN')
        men_totals = process_attendance_worksheet(xlsx_file, 'MEN')
        print('processing WOMEN')
        women_totals = process_attendance_worksheet(xlsx_file, 'WOMEN')
        print('processing YOUTH')
        youth_totals = process_attendance_worksheet(xlsx_file, 'YOUTH')
        print('processing CHILDREN')
        children_totals = process_attendance_worksheet(xlsx_file, 'CHILDREN')
        total = men_totals["Total"] + women_totals["Total"] + youth_totals["Total"] + children_totals["Total"]
        full_result = {
            'men': men_totals,
            'women': women_totals,
            'youth': youth_totals,
            'children': children_totals,
            'total': total 
        }
        
        print(full_result)
        if (men_totals['date'] == None or women_totals['date'] == None
            or (youth_totals['date']== None) or children_totals['date'] == None): 
            messages.warning(request, 'missing date')
            
        url = reverse('admin:index')
        return HttpResponseRedirect('http://localhost:8000/admin/service/attendance/upload-csv/')
    
    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)

def process_attendance_worksheet(xlsx_file, worksheet_name):
    data = pd.read_excel(xlsx_file, sheet_name=worksheet_name,  header=None)
    rows = data.values.tolist()
    date = get_date(rows[0][1])
    items = rows[2:]
    total = 0
    total_absent = 0
    total_present = 0
    
    for p in items:
    #    print(p)
        total += 1
        if(p[2] == 'T' or p[2] == 't'):
            total_present+=1
        else:
            total_absent+=1
    results = {
        "date": date,
        "Total": total,
        "absent": total_absent,
        "present": total_present
    }
    print(total)
    return results
  
  
def get_date(raw):
   if raw and 'pandas._libs.tslibs.timestamps.Timestamp' in str(type(raw)):
       return raw.date()
   else:
       return None