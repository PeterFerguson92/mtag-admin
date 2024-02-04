DEPARTMENTS = (
    ("MEN", "Men's Ministry"),
    ("WOMEN", "Women Ministry"),
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

SOURCE = (
        ('WEBSITE', 'Website',),
        ('BANK TRANSFER', 'Bank Transfer',),
        ('MANUAL', 'Manual',),
    )

ORIGIN = (
        ('WEBSITE', 'Website',),
        ('IMPORT', 'Import',),
        ('MANUAL', 'Manual',),
    )

TRANSACTION_TYPE = (
        ('OFFERING', 'Offering',),
        ('TITHE', 'Tithe',),
        ('FREE DONATION', 'Free Donation'),
    )

SERVICE_TYPE = (
        ('TUESDAY BIBLE STUDIES', 'Tuesday Bible studies',),
        ('FRIDAY_PRAYER_MEETING', 'Friday Prayer Meeting',),
        ('1_SUNDAY_SERVICE', 'Sunday 1st Service',),
        ('2_SUNDAY_SERVICE', 'Sunday 2nd Service'),
    )

SERVICES = (
    ("01-SERVICE", "1st Service"),
    ("02-SERVICE", "2nd Service"),
)