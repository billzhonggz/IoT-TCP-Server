# Generated by Django 2.0.2 on 2018-04-25 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tcp', '0002_auto_20180425_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.ProtectedError, to='tcp.Device'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='alarm',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Alarm', to='tcp.Alarm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='device',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.ProtectedError, to='tcp.Device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alarm',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Alarm', to='tcp.Location'),
        ),
    ]