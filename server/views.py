from django.contrib.auth.models import User, Group
from server.models import TrashStats, TrashPlace, Campus
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import UserSerializer, GroupSerializer, TrashPlaceSerializer, TrashStatsSerializer, CampusSerializer
from django.shortcuts import render


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TrashPlacesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trashPlaces to be viewed or edited.
    """
    queryset = TrashPlace.objects.all()
    serializer_class = TrashPlaceSerializer


class TrashPlacesList(APIView):
    def get(self, request, format=None):
        trashPlaces = TrashPlace.objects.all()
        serializer = TrashPlaceSerializer(trashPlaces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TrashPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrashPlacesDetail(APIView):
    def getObject(self, pk):
        try:
            return TrashPlace.objects.get(pk=pk)
        except TrashPlace.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trashPlace = self.getObject(pk)
        serializer = TrashPlaceSerializer(trashPlace)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        trashPlace = self.getObject(pk)
        serializer = TrashPlaceSerializer(trashPlace, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trashPlace = self.getObject(pk)
        trashPlace.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrashStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trashStats to be viewed or edited.
    """
    queryset = TrashStats.objects.all()
    serializer_class = TrashStatsSerializer


class CampusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campuses to be viewed or edited.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CampusList(APIView):
    def get(self, request, format=None):
        campuses = Campus.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampusDetail(APIView):
    def getObject(self, pk):
        try:
            return Campus.objects.get(pk=pk)
        except Campus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        campus = self.getObject(pk)
        serializer = CampusSerializer(campus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        campus = self.getObject(pk)
        serializer = CampusSerializer(campus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        campus = self.getObject(pk)
        campus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)