from django.urls import path
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .service import (
    archive_members,
    export_service_planning_to_xls,
    export_member_attendace,
    process_attendance_import,
    process_children_attendance_import,
    process_men_attendance_import,
    process_women_attendance_import,
    process_youth_attendance_import,
)
from .models import Absence, Attendance, Member, ServicePlanning
from django.core.exceptions import ObjectDoesNotExist


# Register your models here.
class MemberResource(resources.ModelResource):
    class Meta:
        model = Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    massadmin_exclude = [
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
    ]
    search_fields = ("name", "surname", "postcode")
    fields = (
        "name",
        "middle_name",
        "surname",
        "email",
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
        "active",
    )
    list_display = (
        "member_name",
        "full_address",
        "department",
        "last_seen",
        "created_at",
        "active",
    )
    list_filter = (
        "name",
        "surname",
        "postcode",
        "sex",
        "department",
        "member_type",
        "membership_start",
        "origin",
        "created_at",
        "active",
    )
    search_fields = ["name"]
    readonly_fields = ["last_seen"]
    actions = ["export_attendace_to_xls", "export_men_attendace_to_xls", "export_women_attendace_to_xls", "export_youth_attendace_to_xls", "export_children_attendace_to_xls"]
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
        
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.username == 'root':
            return queryset
        if request.user.username == 'youth_dpt':
            return queryset.filter(department="YOUTH")
        if request.user.username == 'women_dpt':
            return queryset.filter(department="WOMEN")
        if request.user.username == 'men_dpt':
            return queryset.filter(department="MEN")
        if request.user.username == 'children_dpt':
            return queryset.filter(department="CHILDREN")
        return queryset    
    

    @admin.action()
    def export_attendace_to_xls(self, request, queryset):
        response = export_member_attendace(request.user.username)
        return response

    export_attendace_to_xls.short_description = (
        "Export Attendance to XLS"  # short description
    )
    export_attendace_to_xls.acts_on_all = True
    
    @admin.action()
    def export_men_attendace_to_xls(self, request, queryset):
        response = export_member_attendace('men_dpt')
        return response

    export_men_attendace_to_xls.short_description = (
        "Export MEN Attendance to XLS"  # short description
    )
    
    @admin.action()
    def export_women_attendace_to_xls(self, request, queryset):
        response = export_member_attendace('women_dpt')
        return response

    export_women_attendace_to_xls.short_description = (
        "Export WOMEN Attendance to XLS"  # short description
    )
    
    @admin.action()
    def export_youth_attendace_to_xls(self, request, queryset):
        response = export_member_attendace('youth_dpt')
        return response

    export_youth_attendace_to_xls.short_description = (
        "Export YOUTH Attendance to XLS"  # short description
    )
    
    @admin.action()
    def export_children_attendace_to_xls(self, request, queryset):
        response = export_member_attendace('children_dpt')
        return response

    export_children_attendace_to_xls.short_description = (
        "Export CHILDREN Attendance to XLS"  # short description
    )

    @admin.action()
    def archive_member(self, request, queryset):
        response = archive_members(queryset)
        return response

    archive_member.short_description = "Archive member/s"  # short description


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
            path("upload-men-csv/", self.upload_men_csv),
            path("upload-women-csv/", self.upload_women_csv),
            path("upload-youth-csv/", self.upload_youth_csv),
            path("upload-children-csv/", self.upload_children_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        return process_attendance_import(self, request)
    
    def upload_men_csv(self, request):
        return process_men_attendance_import(self, request)
    
    def upload_women_csv(self, request):
        return process_women_attendance_import(self, request)
    
    def upload_youth_csv(self, request):
        return process_youth_attendance_import(self, request)
    
    def upload_children_csv(self, request):
        return process_children_attendance_import(self, request)



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
        "source",
        "reason",
        "contacted",
        "contacted_date",
        "person_of_contact",
    )
    list_display = ("member_name", "last_seen", "contacted", "member_department", "created_at",)
    list_filter = ("member", "member__department", "contacted")
    autocomplete_fields = ["member"]

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.source == "IMPORT":
            return [
                "member",
                "last_seen",
                "source",
            ]
        return []

    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"

    def member_department(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            if instance.member.department:
                return f"{instance.member.department}"
            else:
                return ""
        except ObjectDoesNotExist:
            return "ERROR!!"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.username == 'root':
            return queryset
        if request.user.username == 'youth_dpt':
            return queryset.filter(member__department="YOUTH")
        if request.user.username == 'women_dpt':
            return queryset.filter(member__department="WOMEN")
        if request.user.username == 'men_dpt':
            return queryset.filter(member__department="MEN")
        if request.user.username == 'children_dpt':
            return queryset.filter(member__department="CHILDREN")
        return queryset