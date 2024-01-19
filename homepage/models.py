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
    block_1_title = models.CharField("Block 1 Title", max_length=80)
    block_1_text = models.TextField("Block 1 Text", max_length=120)
    block_2_title = models.CharField("Block 2 Title", max_length=80)
    block_2_text = models.TextField("Block 2 Text", max_length=120)
    block_3_title = models.CharField("Block 3 Title", max_length=80)
    block_3_text = models.TextField("Block 3 Text", max_length=120)
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
    

class AboutUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default='About Us')
    homepage_display_header = models.CharField("Homepage Display Header", max_length=80, blank=True, null=True)
    homepage_display_title = models.CharField("Homepage Display Title", max_length=80)
    homepage_display_text = models.TextField("Homepage Display Text", max_length=120)
    homepage_display_info_1 = models.CharField("Homepage Display Info 1 Title", max_length=80, blank=True, null=True)
    homepage_display_info_1_text = models.TextField("Homepage Display Info 1 Text", max_length=120, blank=True, null=True)
    homepage_display_info_2 = models.CharField("Homepage Display Info 2 Title", max_length=80, blank=True, null=True)
    homepage_display_info_2_text = models.TextField("Homepage Display Info 2 Text", max_length=120, blank=True, null=True)
    
    section_display_header = models.CharField("Section Display Header", max_length=80, blank=True, null=True)
    section_display_title = models.CharField("Section Display Title", max_length=80)
    section_display_text = models.TextField("Section Display Text", max_length=120)
    section_display_info_1 = models.CharField("Section Display Info 1 Title", max_length=80, blank=True, null=True)
    section_display_info_1_text = models.TextField("Section Display Info 1 Text", max_length=120, blank=True, null=True)
    section_display_info_2 = models.CharField("Section Display Info 2 Title", max_length=80, blank=True, null=True)
    section_display_info_2_text = models.TextField("Section Display Info 2 Text", max_length=120, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

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
    aboutUs = models.OneToOneField(AboutUs, on_delete=models.CASCADE, null=True)
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
