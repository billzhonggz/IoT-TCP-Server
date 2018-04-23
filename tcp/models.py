from django.db import models


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
    imei = models.IntegerField

    def __str__(self):
        return self.id


class Location(models.Model):
    time = models.DateTimeField
    initial_locate_duration = models.IntegerField
    lat = models.FloatField
    long = models.FloatField
    height = models.FloatField

    def __str__(self):
        return self.id


class Alarm(models.Model):
    time = models.DateTimeField
    power_voltage = models.FloatField
    backup_voltage = models.FloatField
    lock_status = models.IntegerField
    alarm_status = models.IntegerField
    vibrate_alarm_status = models.IntegerField
    lock_mode = models.IntegerField
    alarm_mode = models.IntegerField
    brushless_control_mode = models.IntegerField

    def __str__(self):
        return self.id
