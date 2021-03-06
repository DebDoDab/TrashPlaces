# Generated by Django 3.0.3 on 2020-03-01 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20200301_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownuser',
            name='permission',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ownuser',
            name='campusId',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='ownuser',
            name='trashPlaceId',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='trashstats',
            name='campusId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.Campus'),
        ),
        migrations.AlterField(
            model_name='trashstats',
            name='trashPlaceId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.TrashPlace'),
        ),
    ]
