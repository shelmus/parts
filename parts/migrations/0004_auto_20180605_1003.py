# Generated by Django 2.0.6 on 2018-06-05 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_auto_20180605_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='shipping',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='part',
            name='type',
            field=models.CharField(choices=[('chassis', 'CHASSIS'), ('memory', 'MEMORY'), ('cpu', 'CPU'), ('hdd', 'HDD'), ('ssd', 'SSD'), ('psu', 'PSU'), ('other', 'OTHER'), ('network', 'NETWORK')], max_length=100),
        ),
    ]
