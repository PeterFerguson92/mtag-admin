import uuid
from django.db import models
from constants import ABSENCE_SOURCE, DEPARTMENTS, MEMBER_TYPE, ORIGIN, SERVICES, SEX_CHOICES

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255,blank=False )
    middle_name = models.CharField("Middle Name", max_length=255,blank=True)
    surname = models.CharField("Surname", max_length=255,blank=False)
    telephone = models.CharField("Telephone", max_length=255, blank=True, null=True)
    postcode = models.CharField("Postcode",max_length=255, blank=True, null=True)
    house_number = models.CharField("House Number", blank=True, null=True, max_length=20)
    address = models.CharField("Address",max_length=255, blank=True, null=True)
    date_of_birth = models.DateField("Date Of Birth", blank=True, null=True)
    age = models.IntegerField("Age", blank=True, null=True)
    sex = models.CharField(max_length=50,choices=SEX_CHOICES, blank=True, null=True)
    department = models.CharField("Department",max_length=255,choices=DEPARTMENTS, blank=True, null=True)
    member_type = models.CharField("Member type",max_length=255,choices=MEMBER_TYPE, default='Full Member',  blank=True, null=True)
    origin = models.CharField("Origin",max_length=255,choices=ORIGIN, default='Manual',  blank=True, null=True)
    membership_start = models.DateField("Membership start", max_length=255, blank=True, null=True)
    last_seen = models.DateField("Last seen", auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name","surname","member_type","postcode", "origin", "created_at")
        verbose_name_plural = "Members"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.middle_name} {self.surname}"

class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField("Date")
    number_of_mens = models.IntegerField("Number of Men's", blank=True, null=True)
    number_of_women = models.IntegerField("Number of Women's", blank=True, null=True)
    number_of_youth = models.IntegerField("Number of Youth's", blank=True, null=True)
    number_of_children = models.IntegerField("Number of Children's", blank=True, null=True)
    total = models.IntegerField("Total", blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("date", "created_at")
        verbose_name = "Service Attendance"
        verbose_name_plural = "Service Attendance"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.date, self.created_at)

    def __str__(self):
        return f"{self.date}"

class Absence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='absent_member'
    )
    contact_phone_number = models.CharField("Contact Phone Number", max_length=255)
    last_seen = models.DateField("Last seen")
    reason = models.TextField("Reason", max_length=255,blank=True)
    source = models.CharField("Source",max_length=255,choices=ABSENCE_SOURCE, default='IMPORT',  blank=True, null=True)
    contacted = models.BooleanField("Contacted", default=False )
    contacted_date = models.DateField("Contacted Date", blank=True, null=True)
    person_of_contact = models.CharField("Person of contact",max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("member", "created_at")
        verbose_name_plural = "Member Absence"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.member, self.created_at)

    def __str__(self):
        return f"{self.member}"
    
class ServicePlanning(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Sunday Service")
    service_type = models.CharField(
        "Service Type", max_length=255, choices=SERVICES, blank=False, null=False
    )
    date = models.DateField("Date", editable=True, blank=False, null=False)
    
    mc = models.CharField("MC", max_length=255, blank=True, null=True)
    mc_start_time = models.TimeField("MC Start Time", editable=True,blank=True, null=True)
    mc_end_time = models.TimeField("MC End Time", editable=True,blank=True, null=True)
    expected_mc = models.CharField("Expected MC", max_length=255,blank=True, null=True)
    expected_mc_start_time = models.TimeField("Expected MC Start Time", editable=True,blank=True, null=True)
    expected_mc_end_time = models.TimeField("Expected MC End Time", editable=True,blank=True, null=True)
    
    worship_praise = models.CharField("Worship and Praise", max_length=255, blank=True, null=True)
    worship_praise_start_time = models.TimeField("Worship and Praise Start Time", editable=True,blank=True, null=True)
    worship_praise_end_time = models.TimeField("Worship and Praise End Time", editable=True,blank=True, null=True)
    expected_worship_praise = models.CharField(
        "Expected Worship and Praise", max_length=255,blank=True, null=True
    )
    expected_worship_praise_start_time = models.TimeField("Expected Worship and Praise Time", editable=True,blank=True, null=True)
    expected_worship_praise_end_time = models.TimeField("Expected Worship and Praise End Time", editable=True,blank=True, null=True)
    
    bible_reading = models.CharField("Bible Reading", max_length=255,blank=True, null=True)
    bible_reading_start_time = models.TimeField("Bible Reading Start Time", editable=True,blank=True, null=True)
    bible_reading_end_time = models.TimeField("Bible Reading End Time", editable=True,blank=True, null=True)

    expected_bible_reading = models.CharField("Expected Bible Reading", max_length=255,blank=True, null=True)
    expected_bible_reading_start_time = models.TimeField("Expected Bible Reading Start Time", editable=True,blank=True, null=True)
    expected_bible_reading_end_time = models.TimeField("Expected Bible Reading End Time", editable=True,blank=True, null=True)
    
    mtag_news = models.CharField("MTAG news", max_length=255, blank=True, null=True)
    mtag_news_start_time = models.TimeField("MTAG news Start Time", editable=True,blank=True, null=True)
    mtag_news_end_time = models.TimeField("MTAG news End Time", editable=True,blank=True, null=True)
    expected_mtag_news = models.CharField("Expected MTAG news", max_length=255, blank=True, null=True)
    expected_mtag_news_start_time = models.TimeField("Expected MTAG news Start Time", editable=True,blank=True, null=True)
    expected_mtag_news_end_time = models.TimeField("Expected MTAG news End Time", editable=True,blank=True, null=True)
    
    offering_ministration = models.CharField("Offering & Ministration", max_length=255, blank=True, null=True)
    offering_ministration_start_time = models.TimeField("Offering & Ministration Start Time", editable=True,blank=True, null=True)
    offering_ministration_end_time = models.TimeField("Offering & Ministration End Time", editable=True,blank=True, null=True)
    expected_offering_ministration = models.CharField(
        "Expected Offering & Ministration", max_length=255, blank=True, null=True
    )
    expected_offering_ministration_start_time = models.TimeField("Expected Offering & Ministration Start Time", editable=True,blank=True, null=True)
    expected_offering_ministration_end_time = models.TimeField("Expected Offering & Ministration End Time", editable=True,blank=True, null=True)
    
    sermon = models.CharField("Sermon", max_length=255, blank=True, null=True)
    sermon_start_time = models.TimeField("Sermon Start Time", editable=True,blank=True, null=True)
    sermon_end_time = models.TimeField("Sermon End Time", editable=True,blank=True, null=True)
    expected_sermon = models.CharField("Expected Sermon", max_length=255, blank=True, null=True)
    expected_sermon_start_time = models.TimeField("Expected Sermon Start Time", editable=True,blank=True, null=True)
    expected_sermon_end_time = models.TimeField("Expected Sermon End Time", editable=True,blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("service_type", "date", "created_at")
        verbose_name_plural = "Service Planning"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title} {self.service_type} {self.date}"
    