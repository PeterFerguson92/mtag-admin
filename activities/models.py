import uuid
from django.db import models
from .uploadfiles import (event_upload_image_path)

DAYS = (
    ("01-MONDAY", "Monday"),
    ("02-TUESDAY", "Tuesday"),
    ("03-WEDNESDAY", "Wednesday"),
    ("04-THURSDAY", "Thursday"),
    ("05-FRIDAY", "Friday"),
    ("06-SATURDAY", "Saturday"),
    ("07-SUNDAY", "Sunday"),
)

MONTH = (
    ("01-JANUARY", "January"),
    ("02-FEBRUARY", "February"),
    ("03-MARCH", "March"),
    ("04-APRIL", "April"),
    ("05-MAY", "May"),
    ("06-JUNE", "June"),
    ("07-JULY", "July"),
    ("08-AUGUST", "August"),
    ("09-SEPTEMBER", "September"),
    ("10-OCTOBER", "October"),
    ("11-NOVEMBER", "November"),
    ("12-DECEMBER", "December"),
)


# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description", max_length=1024)
    day = models.CharField("Day", max_length=255, choices=DAYS, blank=True, null=True)
    start_date = models.DateField("Start Date", editable=True, blank=True, null=True)
    end_date = models.DateField("End Date", editable=True, blank=True, null=True)
    start_time = models.TimeField("Start Time", editable=True, blank=True, null=True)
    end_time = models.TimeField("End Time", editable=True, blank=True, null=True)
    location = models.CharField("Location", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=event_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.description,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"


class Weekly(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Weekly Activities")
    events = models.ManyToManyField(to=Event)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Weekly Activities"
        verbose_name_plural = "Weekly Activities"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"

class Monthly(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Monthly Activities")
    month = models.CharField("Month", max_length=255, choices=MONTH, blank=False, null=False)
    events = models.ManyToManyField(to=Event)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Monthly Activities"
        verbose_name_plural = "Monthly Activities"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.month,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title} {self.month}"