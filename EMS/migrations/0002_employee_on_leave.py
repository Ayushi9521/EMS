# Generated by Django 4.0.4 on 2022-04-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='on_leave',
            field=models.BooleanField(default=False),
        ),
    ]
