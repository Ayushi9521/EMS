# Generated by Django 4.0.4 on 2022-04-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0002_employee_on_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Leave_count',
            field=models.IntegerField(default=0),
        ),
    ]
