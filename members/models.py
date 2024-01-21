from django.db import models

DEPARTMENTS = (
    ("MEN", "Men's Ministry"),
    ("WOMEN", "Children's Ministry"),
    ("YOUTH", "Youth Ministry"),
    ("CHILDREN", "Children Ministry"),

)

MEMBER_TYPE = (
    ("FULL MEMBER", "Full Member"),
    ("VISITOR", "Visitor"),
)

SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
    )

ORIGIN = (
        ('WEBSITE', 'Website',),
        ('IMPORT', 'Import',),
        ('MANUAL', 'Manual',),
    )

# Create your models here.
class Member(models.Model):
    name = models.CharField("Name", max_length=255,blank=False )
    middle_name = models.CharField("Middle Name", max_length=255,blank=True)
    surname = models.CharField("Surname", max_length=255,blank=False)
    telephone = models.CharField("Telephone", max_length=255,blank=False)
    postcode = models.CharField("Postcode",max_length=255, blank=True, null=True)
    address = models.CharField("Address",max_length=255, blank=True, null=True)
    date_of_birth = models.CharField("Date Of Birth",max_length=255, blank=True, null=True)
    age = models.IntegerField("Age", blank=True, null=True)
    sex = models.CharField(max_length=50,choices=SEX_CHOICES)
    department = models.CharField("Department",max_length=255,choices=DEPARTMENTS, blank=True, null=True)
    member_type = models.CharField("Member type",max_length=255,choices=MEMBER_TYPE, default='Full Member')
    origin = models.CharField("Origin",max_length=255,choices=ORIGIN, default='Manual')
    membership_start = models.DateField("Membership start", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Members"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name} {self.middle_name} {self.surname}"