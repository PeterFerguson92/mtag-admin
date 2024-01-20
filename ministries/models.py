import uuid
from django.db import models

from ministries.uploadfiles import ministries_upload_image_path, ministry_cover_image_restriction, ministry_gallery_image_restriction

# Create your models here.
class Ministry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    short_description = models.TextField("Short Description", max_length=400, default='')
    description = models.TextField("Long Description", max_length=1024, blank=True, null=True)
    cover_image_path = models.ImageField(
        "Cover image",
        validators=[ministry_cover_image_restriction],
        upload_to=ministries_upload_image_path,
    )
    gallery_image_path_1 = models.ImageField(
        "Gallery image 1",
        validators=[ministry_gallery_image_restriction],
        upload_to=ministries_upload_image_path,
        null=True,
        blank=True,
    ) 
    gallery_image_path_2 = models.ImageField(
        "Gallery image 2",
        validators=[ministry_gallery_image_restriction],
        upload_to=ministries_upload_image_path,
        null=True,
        blank=True,
    )
    gallery_image_path_3 = models.ImageField(
        "Gallery image 3",
        validators=[ministry_gallery_image_restriction],
        upload_to=ministries_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Ministries"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.name}"