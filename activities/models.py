from django.db import models
import uuid

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
    day = models.CharField("Day", max_length=255, choices=DAYS, blank=False, null=False)
    time = models.TimeField(
        "Time", auto_now=False, auto_now_add=False, blank=False, null=False
    )
    date = models.DateField("Date", editable=True, blank=True, null=True)
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
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"