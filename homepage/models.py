import uuid
from django.db import models
from homepage.uploadfiles import *
from django_resized import ResizedImageField

# Create your models here.
POSITIONS = (
    ("left", "left"),
    ("right", "right"),
)

class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Text", blank=True, null=True)
    image = ResizedImageField(
        "Image",
        size=[203, 223],
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
    title = models.CharField("Title", max_length=255, default="Block Section")
    block_1_title = models.CharField("Block 1 Title", max_length=500)
    block_1_text = models.TextField("Block 1 Text")
    block_2_title = models.CharField("Block 2 Title", max_length=500)
    block_2_text = models.TextField("Block 2 Text")
    block_3_title = models.CharField("Block 3 Title", max_length=500)
    block_3_text = models.TextField("Block 3 Text")
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
    title = models.CharField("Title", max_length=255, default="About Us")
    homepage_display_header = models.CharField(
        "Homepage Display Header", max_length=500, blank=True, null=True
    )
    homepage_display_title = models.CharField("Homepage Display Title", max_length=500)
    homepage_display_text = models.TextField("Homepage Display Text")
    homepage_display_info_1 = models.CharField(
        "Homepage Display Info 1 Title", max_length=80, blank=True, null=True
    )
    homepage_display_info_1_text = models.TextField(
        "Homepage Display Info 1 Text", blank=True, null=True
    )
    homepage_display_info_2 = models.CharField(
        "Homepage Display Info 2 Title", max_length=500, blank=True, null=True
    )
    homepage_display_info_2_text = models.TextField(
        "Homepage Display Info 2 Text", blank=True, null=True
    )
    homepage_image = ResizedImageField(
        "Homepage Image",
        size=[371, 421],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    section_display_header = models.CharField(
        "Section Display Header", max_length=80, blank=True, null=True
    )
    section_display_title = models.CharField("Section Display Title", max_length=80)
    section_display_text = models.TextField("Section Display Text")
    section_display_info_1 = models.CharField(
        "Section Display Info 1 Title", max_length=80, blank=True, null=True
    )
    section_display_info_1_text = models.TextField(
        "Section Display Info 1 Text", blank=True, null=True
    )
    section_display_info_2 = models.CharField(
        "Section Display Info 2 Title", max_length=80, blank=True, null=True
    )
    section_display_info_2_text = models.TextField(
        "Section Display Info 2 Text", blank=True, null=True
    )

    image_1 = ResizedImageField(
        "Image 1",
        size=[271, 301],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_2 = ResizedImageField(
        "Image 2",
        size=[271, 301],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_3 = ResizedImageField(
        "Image 3",
        size=[271, 301],
        upload_to=homepage_about_us_cover_upload_image_path,
        null=True,
        blank=True,
    )
    image_4 = ResizedImageField(
        "Image 4",
        size=[271, 301],
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
    title = models.CharField("Title", max_length=255, default="Church Details")
    info_text_1 = models.CharField("Info Text 1", max_length=80, blank=True, null=True)
    info_content_1 = models.CharField(
        "Info Content 1", max_length=80, blank=True, null=True
    )
    info_text_2 = models.CharField("Info Text 2", max_length=80, blank=True, null=True)
    info_content_2 = models.CharField(
        "Info Content 2", max_length=80, blank=True, null=True
    )
    address = models.CharField("Address", max_length=500, blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
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
    description = models.TextField("Description", blank=True, null=True)
    date = models.DateField("Date", blank=True, null=True)
    image = ResizedImageField(
        "Image",
        size=[561, 430],
        upload_to=homepage_video_cover_upload_image_path,
        null=True,
        blank=True,
    )
    url = models.CharField("Url", max_length=255)
    featured = models.BooleanField("Featured", default=False)
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


class Broadcast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=80)
    subtitle = models.CharField("Subtitle", max_length=80, blank=True, null=True)
    preview_image = ResizedImageField(
        "Preview Image",
        size=[561, 430],
        upload_to=homepage_video_cover_upload_image_path,
        null=True,
        blank=True,
    )
    link = models.CharField("Link", max_length=255)
    stream_title = models.CharField("Stream Title", max_length=80)
    stream_subtitle = models.CharField(
        "Stream Subtitle", max_length=80, blank=True, null=True
    )
    stream_description = models.TextField(
        "Description", blank=True, null=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Broadcast"
        verbose_name_plural = "Broadcast"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"


class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        "Title",
        default="Social Media Links",
        max_length=255,
    )
    facebook_link = models.CharField("Facebook Link", max_length=255)
    tiktok_link = models.CharField("Tik Tok Link", max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=80, default="Media")
    videos_header = models.CharField(
        "Video Section Header", max_length=80, blank=True, null=True
    )
    videos_title = models.CharField(
        "Video Section Title", max_length=80, blank=True, null=True
    )
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
    description = models.TextField("Description")
    phone = models.CharField("Phone Number", max_length=100)
    address = models.CharField("Address", max_length=200, blank=True, null=True)
    image = ResizedImageField(
        "Image",
        size=[466, 494],
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
    title = models.CharField("Title", max_length=80, default="Leadership Board")
    header = models.CharField("Section Header", max_length=80, blank=True, null=True)
    section_title = models.CharField(
        "Section Title", max_length=80, blank=True, null=True
    )
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
    banners = models.ManyToManyField(to=Banner, blank=True, null=True)
    blocks = models.OneToOneField(
        Block, on_delete=models.CASCADE, blank=True, null=True
    )
    aboutUs = models.OneToOneField(
        AboutUs, on_delete=models.CASCADE, blank=True, null=True
    )
    details = models.OneToOneField(
        Details, on_delete=models.CASCADE, blank=True, null=True
    )
    media = models.OneToOneField(Media, on_delete=models.CASCADE, blank=True, null=True)
    leadershipBoard = models.OneToOneField(
        LeadershipBoard, on_delete=models.CASCADE, blank=True, null=True
    )
    banner_background_image = ResizedImageField(
        "Banner Background Image",
        size=[1921, 905],
        upload_to=homepage_background_upload_image_path,
        null=True,
        blank=True,
    )
    leadership_board_background_image = ResizedImageField(
        "Leadership Board Background Image",
        size=[1921, 905],
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
