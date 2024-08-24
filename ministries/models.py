import uuid
from django.db import models


# Create your models here.
class Ministry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    short_description = models.TextField("Short Description", max_length=400, default='')
    description = models.TextField("Long Description", max_length=1024, blank=True, null=True)
    cover_image_path = models.CharField("Cover Image", max_length=255, blank=True, null=True)
    gallery_image_path_1 = models.CharField("Gallery image 1", max_length=255, blank=True, null=True)
    gallery_image_path_2 = models.CharField("Gallery image 2", max_length=255, blank=True, null=True)
    gallery_image_path_3 = models.CharField("Gallery image 3", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Ministries"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.name}"