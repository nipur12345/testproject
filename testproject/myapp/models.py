from django.db import models
from timezone_field import TimeZoneFormField
from datetime import datetime
# Create your models here.
class Activity_periods(models.Model):
    start_time=models.DateTimeField(default=datetime.today)
    end_time=models.DateTimeField(default=datetime.today)
class Members(models.Model):
    member_id=models.CharField(max_length=10,default="")
    realname=models.CharField(max_length=30,default="")
    tz=models.CharField(max_length=50,default="")
    activity_periods=models.ManyToManyField(Activity_periods)
    def __str__(self):
        return self.realname

