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

ABSENCE_SOURCE = (
        ('IMPORT', 'Import',),
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
         ('OTHER', 'Other'),
    )

SERVICE_TYPE = (
        ('TUESDAY BIBLE STUDIES', 'Tuesday Bible studies',),
        ('FRIDAY_PRAYER_MEETING', 'Friday Prayer Meeting',),
        ('1_SUNDAY_SERVICE', 'Sunday 1st Service',),
        ('2_SUNDAY_SERVICE', 'Sunday 2nd Service'),
        ('3_SUNDAY_SERVICE', 'Sunday 3rd Service',),
    )

SERVICES = (
    ("01-SERVICE", "1st Service"),
    ("02-SERVICE", "2nd Service"),
    ("03-SERVICE", "3rd Service"),
    ("04-SERVICE", "Joint Service"),
)


DAYS = (
    ("01-MONDAY", "Monday"),
    ("02-TUESDAY", "Tuesday"),
    ("03-WEDNESDAY", "Wednesday"),
    ("04-THURSDAY", "Thursday"),
    ("05-FRIDAY", "Friday"),
    ("06-SATURDAY", "Saturday"),
    ("07-SUNDAY", "Sunday"),
    ("08-SUNDAY", "Sunday 1st Service"),
    ("09-SUNDAY", "Sunday 2nd Service"),

)

MONTH = (
    ("01-JANUARY", "January"),
    ("02-FEBRUARY", "February"),
    ("03-MARCH", "March"),
    ("04-APRIL", "April"),
    ("05-MAY", "May"),
    ("06-JUNE", "June"),
    ("07-JULY", "July"),
    ("08-AUGUST", "August"),
    ("09-SEPTEMBER", "September"),
    ("10-OCTOBER", "October"),
    ("11-NOVEMBER", "November"),
    ("12-DECEMBER", "December"),
)

EXCEL_1_SERVICE_INFO = { "index": 2, "description": "01-SERVICE"}
EXCEL_2_SERVICE_INFO = { "index": 3, "description": "02-SERVICE"}
EXCEL_3_SERVICE_INFO = { "index": 4, "description": "03-SERVICE"}
EXCEL_JOINT_SERVICE_INFO = { "index": 5, "description": "04-JOINT SERVICE"}

EXCEL_SERVICES = [EXCEL_1_SERVICE_INFO, EXCEL_2_SERVICE_INFO, EXCEL_3_SERVICE_INFO, EXCEL_JOINT_SERVICE_INFO]