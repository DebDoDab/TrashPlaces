# Generated by Django 3.0.3 on 2020-03-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20200301_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstimatedTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimatedTime', models.DateTimeField()),
                ('campusId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.Campus')),
            ],
        ),
    ]