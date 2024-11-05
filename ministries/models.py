import uuid
from django.db import models
from django_resized import ResizedImageField

from ministries.uploadfiles import ministries_upload_image_path

# Create your models here.
class Ministry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name")
    short_description = models.TextField("Short Description", default='')
    description = models.TextField("Long Description", blank=True, null=True)
    cover_image_path = ResizedImageField(
        "Cover image",
        size=[421, 371],
        upload_to=ministries_upload_image_path,
    )
    gallery_image_path_1 = ResizedImageField(
        "Gallery image 1",
        size=[370, 370],
        upload_to=ministries_upload_image_path,
        null=True,
        blank=True,
    ) 
    gallery_image_path_2 = ResizedImageField(
        "Gallery image 2",
        size=[370, 370],
        upload_to=ministries_upload_image_path,
        null=True,
        blank=True,
    )
    gallery_image_path_3 = ResizedImageField(
        "Gallery image 3",
        size=[370, 370],
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