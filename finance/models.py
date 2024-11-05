import uuid
from django.db import models
from constants import MONTH, SERVICE_TYPE, SOURCE, TRANSACTION_TYPE
from servicemanagement.models import Member

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField("Type",choices=TRANSACTION_TYPE)
    specific_transaction_type = models.CharField("Specific transaction type",blank=True, null=True)
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='members'
    )
    message = models.TextField("Message", blank=True, null=True)
    service_type = models.CharField("Service Type",choices=SERVICE_TYPE, blank=True, null=True)
    date = models.DateField("Date")
    month = models.CharField("Month", choices=MONTH, editable=False)
    source = models.CharField("Source",choices=SOURCE, default='Manual', blank=True, null=True)
    opted_in_gift_aid_donation = models.BooleanField("Opted in gift aid donation", default=False ) 
    gift_aid_donation_occurence = models.CharField("Gift aid donation occurence", blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("type", "created_at")
        verbose_name_plural = "Transactions"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.type, self.created_at)

    def __str__(self):
        return f"{self.type} - {self.member.name} {self.member.surname}"
    
    @property
    def get_month(self): 
        print(self.date)
        if self.date:
           month_index = self.date.month
           return MONTH[month_index - 1][0]
        return None
           
    def save(self, *args, **kwargs):
        self.month = self.get_month
        super().save(*args, **kwargs)

class BankAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name",blank=False )
    account_holder_name = models.CharField("Account Holder Name",blank=False )
    account_number = models.CharField("Account Number",blank=False )
    sort_code = models.CharField("Sort code",blank=False )
    iban = models.CharField("IBAN",blank=True )
    swift_bic = models.CharField("SWIFT BIC",blank=True )  
    visible = models.BooleanField("Visible", default=False )       
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "account_holder_name","created_at")
        verbose_name_plural = "Bank Account Details"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} - {self.account_holder_name}"