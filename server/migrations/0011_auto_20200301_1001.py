# Generated by Django 3.0.3 on 2020-03-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20200301_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusstats',
            name='estimatedTime',
            field=models.TimeField(),
        ),
    ]
