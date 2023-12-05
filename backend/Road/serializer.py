from rest_framework import serializers
from Road.models import Road
from Road.models import Point


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'