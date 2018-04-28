from django.contrib import admin
from .models import *


@admin.register(Device)
class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'imei')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'initial_locate_duration', 'lat', 'long', 'height')


@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'time', 'power_voltage', 'backup_voltage', 'lock_status', 'alarm_status', 'vibrate_alarm_status',
        'lock_mode', 'alarm_mode', 'brushless_control_mode')


@admin.register(RawData)
class RawDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'receive_date_time', 'raw_data')


@admin.register(ServerOperation)
class ServerOperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_change_date_time', 'status')
