# Generated by Django 2.0.6 on 2018-06-05 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
