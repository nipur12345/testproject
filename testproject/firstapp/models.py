from django.db import models
from django.utils import timezone
from timezone_field import TimeZoneFormField
from _datetime import datetime

# Create your models here.
class Activity_Periods(models.Model):
    start_time=models.DateTimeField(default=datetime.today)
    end_time=models.DateTimeField(default=datetime.today)
class Members(models.Model):
    member_id=models.CharField(max_length=10)
    real_name=models.CharField(max_length=30)
    tz=TimeZoneFormField()
    activity_periods=Activity_Periods
