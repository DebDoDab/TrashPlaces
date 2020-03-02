# Generated by Django 3.0.3 on 2020-02-29 21:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrashPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('status', models.IntegerField(choices=[(0, 'Empty trash can'), (1, 'Filled trash can'), (2, 'No trash can')])),
                ('floor', models.IntegerField(default=-1)),
                ('description', models.CharField(default='', max_length=200)),
                ('deployDate', models.DateField(default=django.utils.timezone.now)),
                ('campusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trashplaces', to='server.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='TrashStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleanDate', models.DateField()),
                ('campusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Campus')),
                ('trashPlaceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.TrashPlace')),
            ],
        ),
    ]
