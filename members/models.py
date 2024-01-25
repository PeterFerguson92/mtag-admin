import uuid
from django.db import models

from activities.models import MONTH

DEPARTMENTS = (
    ("MEN", "Men's Ministry"),
    ("WOMEN", "Children's Ministry"),
    ("YOUTH", "Youth Ministry"),
    ("CHILDREN", "Children Ministry"),

)

MEMBER_TYPE = (
    ("FULL MEMBER", "Full Member"),
    ("VISITOR", "Visitor"),
)

SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
    )

SOURCE = (
        ('WEBSITE', 'Website',),
        ('BANK TRANSFER', 'Bank Transfer',),
        ('MANUAL', 'Manual',),
    )

ORIGIN = (
        ('WEBSITE', 'Website',),
        ('IMPORT', 'Import',),
        ('MANUAL', 'Manual',),
    )

TRANSACTION_TYPE = (
        ('OFFERING', 'Offering',),
        ('TITHE', 'Tithe',),
        ('FREE DONATION', 'Free Donation'),
    )

SERVICE_TYPE = (
        ('FRIDAY_PRAYER_MEETING', 'Friday Prayer Meeting',),
        ('1_SUNDAY_SERVICE', 'Sunday 1st Service',),
        ('2_SUNDAY_SERVICE', 'Sunday 2nd Service'),
    )

# Create your models here.
class Member(models.Model):
    name = models.CharField("Name", max_length=255,blank=False )
    middle_name = models.CharField("Middle Name", max_length=255,blank=True)
    surname = models.CharField("Surname", max_length=255,blank=False)
    telephone = models.CharField("Telephone", max_length=255, blank=True, null=True)
    postcode = models.CharField("Postcode",max_length=255, blank=True, null=True)
    house_number = models.IntegerField("House Number", blank=True, null=True)
    address = models.CharField("Address",max_length=255, blank=True, null=True)
    date_of_birth = models.CharField("Date Of Birth",max_length=255, blank=True, null=True)
    age = models.IntegerField("Age", blank=True, null=True)
    sex = models.CharField(max_length=50,choices=SEX_CHOICES, blank=True, null=True)
    department = models.CharField("Department",max_length=255,choices=DEPARTMENTS, blank=True, null=True)
    member_type = models.CharField("Member type",max_length=255,choices=MEMBER_TYPE, default='Full Member',  blank=True, null=True)
    origin = models.CharField("Origin",max_length=255,choices=ORIGIN, default='Manual',  blank=True, null=True)
    membership_start = models.DateField("Membership start", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Members"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.middle_name} {self.surname}"

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField("Type",max_length=255,choices=TRANSACTION_TYPE)
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='members'
    )
    message = models.TextField("Message", max_length=1024, blank=True, null=True)
    service_type = models.CharField("Service Type",max_length=255,choices=SERVICE_TYPE, blank=True, null=True)
    date = models.DateField("Date",max_length=255)
    month = models.CharField("Month", max_length=255, choices=MONTH, blank=False, null=False)
    source = models.CharField("Source",max_length=255,choices=SOURCE, default='Manual',  blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("type", "created_at")
        verbose_name_plural = "Transactions"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.type, self.created_at)

    def __str__(self):
        return f"{self.type} - {self.member.name} {self.member.surname}"
    
    