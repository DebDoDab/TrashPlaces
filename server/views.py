from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
from server.models import TrashStats, TrashPlace, Campus, OwnPermission, CampusStats
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, GroupSerializer, TrashPlaceSerializer, TrashStatsSerializer, CampusSerializer
from .serializers import OwnPermissionSerializer, CampusStatsSerializer
from django.shortcuts import render
from rest_framework import generics
from django.utils.timezone import now
import datetime
from django.http import HttpResponse
from django.http import response
from itertools import chain


class CampusStatsViewSet(viewsets.ModelViewSet):
    queryset = CampusStats.objects.all()
    serializer_class = CampusStatsSerializer

    def get_queryset(self):
        queryset = CampusStats.objects.all()

        campusId = self.request.query_params.get('campusId', None)
        print(campusId)
        if campusId is None:
            return queryset

        queryset = queryset.filter(campusId_id=campusId)

        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class OwnPermissionViewSet(viewsets.ModelViewSet):
    queryset = OwnPermission.objects.all()
    serializer_class = OwnPermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TrashPlacesViewSet(viewsets.ModelViewSet):
    queryset = TrashPlace.objects.all().order_by('-deployDate')
    serializer_class = TrashPlaceSerializer

    def get_queryset(self):
        queryset = TrashPlace.objects.all()
        user = self.request.user
        permissions = OwnPermission.objects.filter(user=user)
        print(permissions, permissions.count())
        if permissions.count() == 0:
            return queryset.filter(status=-1)

        permission = permissions[0]
        print(repr(permission.content_type))

        if permission.permission == 1:
            return queryset.filter(id=permission.trashPlaceId)
        elif permission.permission == 2:
            return queryset.filter(campusId=permission.campusId)

        return queryset


class TrashStatsViewSet(viewsets.ModelViewSet):
    queryset = TrashStats.objects.all()
    serializer_class = TrashStatsSerializer

    def get_queryset(self):
        queryset = TrashStats.objects.all()
        campusId = self.request.query_params.get('campusid', None)
        if campusId is None:
            return queryset
        queryset = queryset.filter(campusId=campusId)
        timeDelta = self.request.query_params.get('timeDelta', None)
        getStats = self.request.query_params.get('getStats', False)
        if timeDelta is None:
            return queryset
        elif timeDelta == "month":
            queryset = queryset.filter(requestDate=now()-timeDelta(days=30))
            return queryset


        # dateFrom = datetime.datetime(self.request.query_params.get('datefrom', now))


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
