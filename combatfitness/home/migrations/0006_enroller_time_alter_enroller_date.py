# Generated by Django 4.1 on 2023-07-19 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_enroller_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroller',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enroller',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]