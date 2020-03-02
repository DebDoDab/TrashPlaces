from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils.timezone import now


class CampusStats(models.Model):
    estimatedTime = models.TimeField()
    themostpopular = models.ForeignKey('TrashPlace', on_delete=models.CASCADE)
    # theleastpopular = models.ForeignKey('TrashPlace', on_delete=models.CASCADE)
    campusId = models.ForeignKey('Campus', on_delete=models.CASCADE)


class Campus(models.Model):
    name = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class TrashPlace(models.Model):
    name = models.CharField(max_length=30, default='')
    STATUS_CHOICES = [
        (0, 'Empty trash can'),
        (1, 'Filled trash can'),
        (2, 'No trash can'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)
    campusId = models.ForeignKey(Campus, related_name='trashplaces', on_delete=models.CASCADE)
    floor = models.IntegerField(default=-1)
    description = models.CharField(max_length=200, default='')
    deployDate = models.DateField(default=now)

    def __str__(self):
        return self.name


class OwnPermission(Permission):
    PERMISSIONS_CHOISE = [
        (0, 'nothing'),
        (1, 'employee'),
        (2, 'operator'),
    ]
    permission = models.IntegerField(choices=PERMISSIONS_CHOISE, default=0)
    trashPlaceId = models.IntegerField(default=-1)
    campusId = models.IntegerField(default=-1)


class TrashStats(models.Model):
    requestDate = models.DateField()
    cleanDate = models.DateField(default=now)
    campusId = models.ForeignKey(Campus, on_delete=models.CASCADE, default=1)
    trashPlaceId = models.ForeignKey(TrashPlace, on_delete=models.CASCADE, default=1)
