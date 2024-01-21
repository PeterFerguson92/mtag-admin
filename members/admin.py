from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "middle_name",
        "surname",
        "telephone",
        "postcode",
        "address",
        "date_of_birth",
        "age",
        "sex",
        "department",
        "member_type",
        "membership_start",
        "origin",
    )
    list_display = ("name", "middle_name", "surname", "member_type", "origin",)
    list_filter = (
        "name",
        "surname",
        "department",
        "member_type",
        "membership_start",
        "origin",
        "created_at",
    )
