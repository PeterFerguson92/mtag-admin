from django.contrib import admin

from .models import Member


@admin.register(Member)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "middle_name",
        "surname",
        "telephone",
        "sex",
        "department"
    )
    list_display = ("name", "middle_name","surname", "created_at")
    list_filter = (
        "name",
        "surname",
        "created_at",
    )