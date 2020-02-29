from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Campus(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class TrashPlace(models.Model):
    campusId = models.ForeignKey(Campus, related_name='trashplaces', on_delete=models.CASCADE)
    floor = models.IntegerField()
    pictureCoordinateX = models.IntegerField()
    pictureCoordinateY = models.IntegerField()
    STATUS_CHOICES = [
        (0, 'Empty trash can'),
        (1, 'Filled trash can'),
        (2, 'No trash can'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.description


class TrashStats(models.Model):
    throwDate = models.DateField()
    trashPlaceId = models.ForeignKey(TrashPlace, on_delete=models.CASCADE)

