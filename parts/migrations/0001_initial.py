# Generated by Django 2.0.6 on 2018-06-04 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('chassis', 'CHASSIS'), ('memory', 'MEMORY'), ('cpu', 'CPU'), ('hdd', 'HDD'), ('ssd', 'SSD'), ('psu', 'PSU'), ('network', 'NETWORK')], max_length=7)),
                ('model', models.TextField()),
                ('brand', models.TextField()),
                ('serial', models.TextField()),
                ('status', models.CharField(choices=[('new', 'NEW'), ('spare', 'SPARE'), ('broken', 'BROKEN'), ('unknown', 'UNKNOWN')], default='new', max_length=7)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
