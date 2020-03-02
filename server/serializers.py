from django.contrib.auth.models import User, Group, ContentType
from rest_framework import serializers
from server.models import TrashPlace, TrashStats, Campus, OwnPermission, CampusStats
import datetime
from django.core.mail import send_mail
import trashcans.settings


class UserSerializer(serializers.ModelSerializer):
    # TODO update method in UserSerializer
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    groups = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='group-detail')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class OwnPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnPermission
        fields = ['url', 'name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # TODO add method in GroupSerializer
    # TODO add Group permissions
    class Meta:
        model = Group
        fields = ['url', 'name']


class CampusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=300)
    trashplaces = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='trashplace-detail')

    def create(self, validated_data):
        newcampus = Campus.objects.create(**validated_data)
        if newcampus:
            ae = ContentType.objects.create(app_label='server', model=User)
            OwnPermission.objects.create(content_type=ae, name=f"{newcampus.name} operator", codename=1, permission=2,
                                         campusId=newcampus.id)
        return newcampus

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

    class Meta:
        model = Campus
        fields = ['url', 'name', 'address', 'trashplaces']


class TrashPlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    STATUS_CHOICES = [
        (0, 'Empty trash can'),
        (1, 'Filled trash can'),
        (2, 'No trash can'),
    ]
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    campusId = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='campus-detail')
    floor = serializers.IntegerField()
    description = serializers.CharField(max_length=200, default='')
    deployDate = serializers.DateField(default=datetime.date.today())

    def create(self, validated_data):
        newtrash = TrashPlace.objects.create(**validated_data)
        if newtrash:
            ae = ContentType.objects.create(app_label='server', model=User)
            OwnPermission.objects.create(content_type=ae, name=f"{newtrash.name} employee", codename=1, permission=1,
                                         campusId=newtrash.id)
        return newtrash

    def update(self, instance, validated_data):
        instance.campusId = Campus.objects.get(id=validated_data.get('campusId', instance.campusId.id))
        instance.name = validated_data.get('name', instance.name)
        cool = False
        if instance.status != 1 and validated_data.get('status', instance.status) == 1:
            cool = True

        if instance.status == 1 and validated_data.get('status', instance.status) != 1:
            TrashStats.objects.create()
        # print(cool)
        instance.status = validated_data.get('status', instance.status)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if cool:
            fulltrashcans = TrashPlace.objects.filter(status=1, campusId=instance.campusId)
            # print(fulltrashcans.count())
            if fulltrashcans.count() == trashcans.settings.TRASH_COUNT_TO_SEND_EMAIL:
                msg = 'Please take them away :(\n'
                for x in fulltrashcans:
                    msg += f'Floor: {x.floor}, description: {x.description}\n'

                print(msg)

                send_mail(
                    'TrashCans are full',
                    msg,
                    trashcans.settings.EMAIL_HOST_USER,
                    ['123ffsa123saaddvs@x3mailer.com']
                )

        return instance

    class Meta:
        model = TrashPlace
        fields = ['url', 'name', 'status', 'campusId', 'floor', 'description', 'description', 'deployDate']


class TrashStatsSerializer(serializers.ModelSerializer):
    # TODO create method in TrashStatsSerializer
    requestDate = serializers.DateField()
    cleanDate = serializers.DateField()
    trashPlaceId = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='trashplace-detail')
    campusId = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='campus-detail')

    class Meta:
        model = TrashStats
        fields = ['url', 'requestDate', 'cleanDate', 'trashPlaceId', 'campusId']


class CampusStatsSerializer(serializers.ModelSerializer):
    estimatedTime = serializers.DateTimeField()
    campusId = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='campus-detail')
    themostpopular = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='trashplace-detail')

    class Meta:
        model = CampusStats
        fields = ['url', 'estimatedTime', 'campusId', 'themostpopular']
