# Generated by Django 4.0.4 on 2022-04-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0005_alter_employee_address_alter_employee_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Active',
            field=models.BooleanField(default=False),
        ),
    ]
