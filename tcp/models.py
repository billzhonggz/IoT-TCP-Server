from django.db import models
from datetime import datetime


# Create your models here.


class RawData(models.Model):
    receive_date_time = models.DateTimeField(auto_now_add=True)
    raw_data = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class ServerOperation(models.Model):
    status_change_date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    def __str__(self):
        return self.id


class Device(models.Model):
    imei = models.BigIntegerField(default=0, unique=True)

    def __str__(self):
        return self.id


class Location(models.Model):
    device = models.ForeignKey(Device, on_delete=models.ProtectedError)
    # alarm = models.OneToOneField(
    #     'Alarm',
    #     on_delete=models.CASCADE,
    #     related_name='Alarm',
    # )
    time = models.DateTimeField(default=datetime.now())
    initial_locate_duration = models.IntegerField(default=0)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)

    def __str__(self):
        return self.id


class Alarm(models.Model):
    device = models.ForeignKey(Device, on_delete=models.ProtectedError)
    # location = models.OneToOneField(
    #     Location,
    #     on_delete=models.CASCADE,
    #     related_name='Alarm',
    # )
    time = models.DateTimeField(default=datetime.now())
    power_voltage = models.FloatField(default=0.0)
    backup_voltage = models.FloatField(default=0.0)
    lock_status = models.IntegerField(default=0)
    alarm_status = models.IntegerField(default=0)
    vibrate_alarm_status = models.IntegerField(default=0)
    lock_mode = models.IntegerField(default=0)
    alarm_mode = models.IntegerField(default=0)
    brushless_control_mode = models.IntegerField(default=0)

    def __str__(self):
        return self.id
