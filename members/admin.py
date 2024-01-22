import decimal
from django.contrib import admin

from .models import Member, Transaction
from django.core.exceptions import ObjectDoesNotExist
import csv
from django.http import HttpResponse


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
    actions = ["export_to_csv",]

    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"

    @admin.action(description="Mark selected stories as published")
    def export_to_csv(modeladmin, request, queryset):
        print(queryset)
        total_amount = decimal.Decimal(0.00)
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment;" "filename={}.csv".format(
            "transaction_outline"
        )
        writer = csv.writer(response)
        writer.writerow(
            [
                "Full Name",
                "Type",
                "Service type",
                "Month",
                "Date",
                "Amount",
            ]
        )
        for s in queryset:
            total_amount = total_amount + s.amount
            writer.writerow(
                [
                    f"{s.member.name} {s.member.middle_name} {s.member.surname}",
                    s.type,
                    s.service_type,
                    s.month,
                    s.date.strftime("%d/%m/%Y"),
                    s.amount,
                ]
            )

        writer.writerow(
            [
                "Total Amount","","","","",total_amount,
            ]
        )
        return response

    export_to_csv.short_description = "Export to CSV"  # short description