from datetime import datetime
from django.contrib import admin
from finance.service import export_transaction_to_xls
from .models import BankAccount, Transaction
from django.core.exceptions import ObjectDoesNotExist
from rangefilter.filters import (
    DateRangeFilterBuilder
)
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("member__name","member__surname","member__postcode", "source")
    fields = (
        "amount",
        "type",
        "specific_transaction_type",
        "message",
        "member",
        "source",
        "date",
        "opted_in_gift_aid_donation",
        "gift_aid_donation_occurence",
        "service_type",
    )
    list_display = ("type", "member_name", "member_postcode_address","date", "month", "source")
    list_filter = ("type", "date", "member", "source", "month", ("date", DateRangeFilterBuilder()))
    autocomplete_fields = ['member']
    actions = ["export_to_xls"]
    
    class Media:
        css = {"all": ("admin/css/forms.css", "css/admin/daterange.css")}
        js = ("admin/js/calendar.js", "js/admin/DateRangeShortcuts.js")

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.source == 'WEBSITE':
            return ["message", "specific_transaction_type"]
        return []
    
    def member_name(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            return f"{instance.member.name}  {instance.member.surname}"
        except ObjectDoesNotExist:
            return "ERROR!!"
    
    def member_postcode_address(
        self, instance
    ):  # name of the method should be same as the field given in `list_display`
        try:
            if(instance.member.postcode and instance.member.house_number):
                return f"{instance.member.postcode} - {instance.member.house_number}"
            else: 
                return ''
        except ObjectDoesNotExist:
            return "ERROR!!"

    @admin.action()
    def export_to_xls(self, request, queryset):
        return export_transaction_to_xls(queryset)

    export_to_xls.short_description = "Export to XLS"  # short description

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "account_holder_name",
        "account_number",
        "sort_code",
        "iban",
        "swift_bic",
        "visible",
    )
    list_display = (
        "name",
        "account_holder_name",
        "visible",
    )