# Generated by Django 2.0.6 on 2018-06-06 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_part_po_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='delete_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='part',
            name='location',
            field=models.CharField(choices=[('LAB', 'LAB'), ('BRAD', 'BRAD'), ('JOSH', 'JOSH'), ('SEAN', 'SEAN'), ('ASBN', 'ASBN'), ('SNVA', 'SNVA')], default='lab', max_length=100),
        ),
        migrations.AlterField(
            model_name='part',
            name='type',
            field=models.CharField(choices=[('chassis', 'CHASSIS'), ('memory', 'MEMORY'), ('cpu', 'CPU'), ('hdd', 'HDD'), ('ssd', 'SSD'), ('psu', 'PSU'), ('other', 'OTHER'), ('optic', 'OPTIC')], max_length=100),
        ),
    ]
