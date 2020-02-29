from django.contrib.auth.models import User, Group
from rest_framework import serializers
from server.models import TrashPlace, TrashStats, Campus


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CampusSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=200)
    # trashplaces = serializers.StringRelatedField(many=True, read_only=True)
    trashplaces = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='trashplace-detail')
    def create(self, validated_data):
        return Campus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('descripton', instance.description)
        instance.save()
        return instance

    class Meta:
        model = Campus
        fields = ['url', 'description', 'trashplaces']


class TrashPlaceSerializer(serializers.Serializer):
    # campusId = CampusSerializer(many=False)
    campusId = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='campus-detail')
    floor = serializers.IntegerField()
    pictureCoordinateX = serializers.IntegerField()
    pictureCoordinateY = serializers.IntegerField()
    STATUS_CHOICES = [
        (0, 'Empty trash can'),
        (1, 'Filled trash can'),
        (2, 'No trash can'),
    ]
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    description = serializers.CharField(max_length=200, default='')

    def create(self, validated_data):
        return TrashPlace.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.campusId = validated_data.get('campusId', instance.campusId)
        instance.floor = validated_data.get('campusId', instance.floor)
        instance.pictureCoordinateX = validated_data.get('campusId', instance.pictureCoordinateX)
        instance.pictureCoordinateY = validated_data.get('campusId', instance.pictureCoordinateY)
        instance.description = validated_data.get('campusId', instance.description)
        instance.status = validated_data.get('campusId', instance.status)
        instance.save()
        return instance

    class Meta:
        model = TrashPlace
        fields = ['campusId', 'floor', 'description', 'status', 'pictureCoordinateX', 'pictureCoordinateY']



class TrashStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrashStats
        fields = ['url', 'throwDate']
