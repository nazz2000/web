# Generated by Django 4.2.16 on 2024-11-06 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managingsystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliance',
            name='appliance_id',
        ),
    ]
