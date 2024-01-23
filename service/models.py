from django.db import models
import uuid

SERVICES = (
    ("01-SERVICE", "1st Service"),
    ("02-SERVICE", "2nd Service"),
)


# Create your models here.
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
        verbose_name_plural = "Service"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title} {self.service_type} {self.date}"
