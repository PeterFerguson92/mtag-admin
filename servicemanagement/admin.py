from django.urls import path
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .service import (
    export_service_planning_to_xls,
    export_member_attendace,
    process_attendance_import,
)
from .models import Absence, Attendance, Member, ServicePlanning
from django.core.exceptions import ObjectDoesNotExist


# Register your models here.
class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    search_fields = ("name", "surname", "postcode")
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
        "member_name",
        "full_address",
        "department",
        "origin",
        "last_seen",
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
    search_fields = ["name"]
    readonly_fields = ["last_seen"]
    actions = ["export_attendace_to_xls"]
    resource_classes = [MemberResource]

    def get_search_results(self, request, queryset, search_term):
        results = super().get_search_results(request, queryset, search_term)
        return results

    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.name} {instance.middle_name} {instance.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"

    def full_address(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.house_number} {instance.address} {instance.postcode}"
        except ObjectDoesNotExist:
            return "ERROR!!"

    @admin.action()
    def export_attendace_to_xls(self, request, queryset):
        response = export_member_attendace()
        return response

    export_attendace_to_xls.short_description = (
        "Export Attendance to XLS"  # short description
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    fields = (
        "date",
        "number_of_mens",
        "number_of_women",
        "number_of_youth",
        "number_of_children",
        "total",
    )
    list_display = (
        "date",
        "created_at",
    )
    list_filter = ("date",)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        return process_attendance_import(self, request)


@admin.action()
def export_to_xls(self, request, queryset):
    # Create a workbook and add a worksheet.
    return export_service_planning_to_xls(queryset)


export_to_xls.short_description = "Export to XLS"  # short description


@admin.register(ServicePlanning)
class ServicePlanningAdmin(admin.ModelAdmin):
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
    list_filter = (
        "date",
        "service_type",
    )
    actions = [export_to_xls]


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    # search_fields = ("title__startswith",)
    fields = (
        "member",
        "last_seen",
        "contact_phone_number",
        "reason",
        "contacted",
        "contacted_date",
        "person_of_contact",
    )
    list_display = (
        "member_name",
        "last_seen",
        "created_at",
    )
    list_filter = ("member",)
    autocomplete_fields = ['member']

    def get_readonly_fields(self, request, obj=None):
        return ["member","last_seen",]
    
    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"