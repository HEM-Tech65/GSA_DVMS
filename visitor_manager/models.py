from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class VisitorLog(models.Model):
    visitor_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    host_name = models.CharField(max_length=100)
    time_in = models.DateTimeField(default=timezone.now)
    time_out = models.DateTimeField(null=True, blank=True)
    is_signed_in = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.visitor_name} - {self.time_in.strftime('%Y-%m-%d %H:%M')}"