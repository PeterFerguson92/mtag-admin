import uuid
from django.db import models
from homepage.uploadfiles import *

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
        validators=[homepage_banner_image_restriction],
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
    homepage_display_text = models.TextField("Homepage Display Text", max_length=180)
    homepage_display_info_1 = models.CharField("Homepage Display Info 1 Title", max_length=80, blank=True, null=True)
    homepage_display_info_1_text = models.TextField("Homepage Display Info 1 Text", max_length=180, blank=True, null=True)
    homepage_display_info_2 = models.CharField("Homepage Display Info 2 Title", max_length=80, blank=True, null=True)
    homepage_display_info_2_text = models.TextField("Homepage Display Info 2 Text", max_length=180, blank=True, null=True)
    homepage_image = models.ImageField(
        "Homepage Image",
        validators=[homepage_about_us_image_restriction],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    section_display_header = models.CharField("Section Display Header", max_length=80, blank=True, null=True)
    section_display_title = models.CharField("Section Display Title", max_length=80)
    section_display_text = models.TextField("Section Display Text", max_length=180)
    section_display_info_1 = models.CharField("Section Display Info 1 Title", max_length=80, blank=True, null=True)
    section_display_info_1_text = models.TextField("Section Display Info 1 Text", max_length=255, blank=True, null=True)
    section_display_info_2 = models.CharField("Section Display Info 2 Title", max_length=80, blank=True, null=True)
    section_display_info_2_text = models.TextField("Section Display Info 2 Text", max_length=255, blank=True, null=True)
    
    image_1 = models.ImageField(
        "Image 1",
        validators=[about_us_image_restriction],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_2 = models.ImageField(
        "Image 2",
        validators=[about_us_image_restriction],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_3 = models.ImageField(
        "Image 3",
        validators=[about_us_image_restriction],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_4 = models.ImageField(
        "Image 4",
        validators=[about_us_image_restriction],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    
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

class Details(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default='Church Details')
    info_text_1 = models.CharField("Info Text 1", max_length=80, blank=True, null=True)
    info_content_1 = models.CharField("Info Content 1", max_length=80, blank=True, null=True)
    info_text_2 = models.CharField("Info Text 2", max_length=80, blank=True, null=True)
    info_content_2 = models.CharField("Info Content 2", max_length=80, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Details"
        verbose_name_plural = "Details"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
    
class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=80)
    description = models.TextField("Description", max_length=180, blank=True, null=True)
    date = models.DateField("Date", blank=True, null=True)
    image = models.ImageField(
        "Image",
        validators=[video_image_restriction],
        upload_to=homepage_video_cover_upload_image_path,
        null=True,
        blank=True,
    )
    url = models.CharField("Url", max_length=255)
    featured=models.BooleanField("Featured", default=False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Video"
        verbose_name_plural = "Video"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=80, default='Media')
    videos_header = models.CharField("Video Section Header", max_length=80, blank=True, null=True)
    videos_title = models.CharField("Video Section Title", max_length=80, blank=True, null=True)
    videos = models.ManyToManyField(to=Video)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"

class Leader(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.CharField("Full Name", max_length=300)
    role = models.CharField("Role", max_length=300)
    description = models.TextField("Description", max_length=700)
    phone = models.CharField("Phone Number", max_length=100)
    address = models.CharField("Address", max_length=200, blank=True, null=True)
    image = models.ImageField(
        "Image",
        validators=[leader_image_restriction],
        upload_to=homepage_leader_cover_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("fullName", "created_at")
        verbose_name = "Leader"
        verbose_name_plural = "Leaders"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.fullName,
            self.created_at,
        )

    def __str__(self):
        return f"{self.fullName}"

class LeadershipBoard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=80, default='Leadership Board')
    header = models.CharField("Section Header", max_length=80, blank=True, null=True)
    section_title = models.CharField("Section Title", max_length=80, blank=True, null=True)
    leaders = models.ManyToManyField(to=Leader)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Leadership Board"
        verbose_name_plural = "Leadership Board"

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
    blocks = models.OneToOneField(Block, on_delete=models.CASCADE, null=True) 
    aboutUs = models.OneToOneField(AboutUs, on_delete=models.CASCADE, null=True)
    details = models.OneToOneField(Details, on_delete=models.CASCADE, null=True)
    media = models.OneToOneField(Media, on_delete=models.CASCADE, null=True)
    leadershipBoard = models.OneToOneField(LeadershipBoard, on_delete=models.CASCADE, null=True)
    banner_background_image = models.ImageField(
        "Banner Background Image",
        validators=[homepage_background_image_restriction],
        upload_to=homepage_background_upload_image_path,
        null=True,
        blank=True,
    )
    leadership_board_background_image = models.ImageField(
        "Leadership Board Background Image",
        validators=[homepage_background_image_restriction],
        upload_to=homepage_background_upload_image_path,
        null=True,
        blank=True,
    )
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
