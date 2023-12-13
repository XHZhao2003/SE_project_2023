from rest_framework import serializers
from Location.models import Location, Comment, TagFunction, TagPlace, TagTime


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
class CommentSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagFunction
        fields = '__all__'
        
class TagPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagPlace
        fields = '__all__'

class TagTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagTime
        fields = '__all__'