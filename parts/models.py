from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('new','NEW'),
    ('spare','SPARE'),
    ('broken','BROKEN'),
    ('recycled',"RECYCLED"),
    ('unknown','UNKNOWN'),
)
TYPE_CHOICES = (
    ('chassis','CHASSIS'), # TODO: subclass for network devices
    ('memory','MEMORY'),
    ('cpu','CPU'),
    ('hdd','HDD'),
    ('ssd','SSD'),
    ('psu','PSU'),
    ('other','OTHER'), # TODO: subclass for nics, video cards, etc.
    ('optic','OPTIC'),
)
LOCATION_CHOICES = (
    ('LAB','LAB'),
    ('BRAD','BRAD'),
    ('JOSH','JOSH'),
    ('SEAN','SEAN'),
    ('ASBN','ASBN'),
    ('SNVA','SNVA'),

)
# Create your models here.
class Part(models.Model):
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='new')
    model = models.TextField()
    brand = models.TextField()
    serial = models.TextField()
    size = models.TextField()
    description = models.TextField() # TODO: this will eventually be filled in by Octopart
    shipping = models.TextField()
    po_number = models.TextField()
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='lab')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def add_part(self):
        self.save()
    def __str__(self):
        return self.serial
