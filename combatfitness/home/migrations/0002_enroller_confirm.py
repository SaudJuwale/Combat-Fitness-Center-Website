# Generated by Django 4.1 on 2023-07-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroller',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]