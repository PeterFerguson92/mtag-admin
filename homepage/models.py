import uuid
from django.db import models
from homepage.uploadfiles import homepage_banner_upload_image_path

# Create your models here.
POSITIONS = (
    ("left", "left"),
    ("right", "right"),
)


class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Text", max_length=1024, blank=True, null=True)
    image = models.ImageField(
        "Image",
        upload_to=homepage_banner_upload_image_path,
        null=True,
        blank=True,
    )
    image_position = models.CharField(
        "position", max_length=255, choices=POSITIONS, blank=True, null=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"

class Block(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default='Block Section')
    block_1_title = models.CharField("Block 1 Title", max_length=255)
    block_1_text = models.TextField("Block 1 Text", max_length=1024)
    block_2_title = models.CharField("Block 2 Title", max_length=255)
    block_2_text = models.TextField("Block 2 Text", max_length=1024)
    block_3_title = models.CharField("Block 3 Title", max_length=255)
    block_3_text = models.TextField("Block 3 Text", max_length=1024)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Block"
        verbose_name_plural = "Blocks"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
    
class Homepage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Homepage")
    banners = models.ManyToManyField(to=Banner)
    blocks = models.ManyToManyField(to=Block)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.id,
            self.created_at,
        )

    def __str__(self):
        return f"{self.id}"
