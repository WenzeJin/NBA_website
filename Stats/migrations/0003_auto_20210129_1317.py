# Generated by Django 3.1.4 on 2021-01-29 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0002_datepicker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datepicker',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]