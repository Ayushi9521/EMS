# Generated by Django 4.0.4 on 2022-04-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0003_employee_leave_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DOJ',
            field=models.TextField(blank=True, null=True),
        ),
    ]