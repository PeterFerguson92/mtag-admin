import uuid
from django.db import models

from constants import DAYS, MONTH
from .uploadfiles import (event_image_restriction, event_upload_image_path)

# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    short_description = models.TextField("Short Description", max_length=400, default='')
    description = models.TextField("Long Description", max_length=1024, blank=True, null=True)
    day = models.CharField("Day", max_length=255, choices=DAYS)
    start_time = models.TimeField("Start Time", editable=True)
    end_time = models.TimeField("End Time", editable=True)
    location = models.CharField("Location", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        validators=[event_image_restriction],
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
    
class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    short_description = models.TextField("Short Description", max_length=400, default='')
    description = models.TextField("Long Description", max_length=1024, blank=True, null=True)
    speaker = models.CharField("speaker", max_length=255, blank=True, null=True)
    start_date = models.DateField("Start Date", editable=True)
    end_date = models.DateField("End Date", editable=True)
    start_time = models.TimeField("Start Time", editable=True)
    end_time = models.TimeField("End Time", editable=True)
    location = models.CharField("Location", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        validators=[event_image_restriction],
        upload_to=event_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.short_description,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"

class Monthly(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Monthly Activities")
    month = models.CharField("Month", max_length=255, choices=MONTH, blank=False, null=False)
    programs = models.ManyToManyField(to=Program)
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
    
# Create your models here.
class SocialEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    short_description = models.TextField("Short Description", max_length=400, default='')
    description = models.TextField("Long Description", max_length=1024, blank=True, null=True)
    day = models.CharField("Day", max_length=255, choices=DAYS)
    start_date = models.DateField("Start Date", editable=True, null=True, blank=True)
    end_date = models.DateField("End Date", editable=True, null=True, blank=True)
    start_time = models.TimeField("Start Time", editable=True)
    end_time = models.TimeField("End Time", editable=True)
    location = models.CharField("Location", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        validators=[event_image_restriction],
        upload_to=event_upload_image_path,
        null=True,
        blank=True,
    )
    gallery_image_path_1 = models.ImageField(
        "Gallery image 1", validators=[event_image_restriction], upload_to=event_upload_image_path, null=True, blank=True
    )
    gallery_image_path_2 = models.ImageField(
        "Gallery image 2", validators=[event_image_restriction], upload_to=event_upload_image_path, null=True, blank=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Social Events"
        verbose_name_plural = "Social Events"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.description,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
