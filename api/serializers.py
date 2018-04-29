from rest_framework import serializers
from tcp.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AlarmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'
