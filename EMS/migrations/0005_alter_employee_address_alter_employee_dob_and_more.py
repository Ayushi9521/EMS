# Generated by Django 4.0.4 on 2022-04-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0004_alter_employee_dob_alter_employee_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DOJ',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]