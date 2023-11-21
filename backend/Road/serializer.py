from rest_framework import serializers
from Road.models import Road


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = [
            "id",
            "name",
            "num_of_points",
            "point_1x",
            "point_1y",
            "point_2x",
            "point_2y",
            "point_3x",
            "point_3y",
            "point_4x",
            "point_4y",
            "base_color",
            "hover_color",
            "feedback_1",
            "feedback_2",
            "feedback_3",
            "feedback_4"
        ]