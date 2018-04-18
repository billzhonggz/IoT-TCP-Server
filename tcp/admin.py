from django.contrib import admin
from .models import RawData, ServerOperation


class RawDataInline(admin.TabularInline):
    model = RawData


class RawDataAdmin(admin.ModelAdmin):
    list_display = ('receive_date_time', 'raw_data')


class ServerOperationInline(admin.TabularInline):
    model = ServerOperation


class ServerOperationAdmin(admin.ModelAdmin):
    list_display = ('status_change_date_time', 'status')


# Register your models here.
admin.site.register(RawData, RawDataAdmin)
admin.site.register(ServerOperation, ServerOperationAdmin)
