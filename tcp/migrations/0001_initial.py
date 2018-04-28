# Generated by Django 2.0.2 on 2018-04-25 08:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2018, 4, 25, 16, 18, 9, 480587))),
                ('power_voltage', models.FloatField(default=0.0)),
                ('backup_voltage', models.FloatField(default=0.0)),
                ('lock_status', models.IntegerField(default=0)),
                ('alarm_status', models.IntegerField(default=0)),
                ('vibrate_alarm_status', models.IntegerField(default=0)),
                ('lock_mode', models.IntegerField(default=0)),
                ('alarm_mode', models.IntegerField(default=0)),
                ('brushless_control_mode', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2018, 4, 25, 16, 18, 9, 480086))),
                ('initial_locate_duration', models.IntegerField(default=0)),
                ('lat', models.FloatField(default=0.0)),
                ('long', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('alarm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Alarm', to='tcp.Alarm')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='tcp.Device')),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date_time', models.DateTimeField(auto_now_add=True)),
                ('raw_data', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ServerOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_change_date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='alarm',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='tcp.Device'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Alarm', to='tcp.Location'),
        ),
    ]
