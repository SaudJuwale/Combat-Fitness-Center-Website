# Generated by Django 4.1 on 2023-07-19 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_enroller_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroller',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
