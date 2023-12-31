from django.db import models
import uuid

DEPARTMENTS = (
    ("MEN", "Men's Ministry"),
    ("WOMEN", "Children's Ministry"),
    ("YOUTH", "Youth Ministry"),
    ("CHILDREN", "Children Ministry"),

)

SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )

# Create your models here.
class Member(models.Model):
    name = models.CharField("Name", max_length=255,blank=False )
    middle_name = models.CharField("Middle Name", max_length=255,blank=True)
    surname = models.CharField("Surname", max_length=255,blank=False)
    telephone = models.CharField("Telephone", max_length=255,blank=False)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    department = models.CharField(max_length=255,choices=DEPARTMENTS)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Members"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.middle_name} {self.surname}"