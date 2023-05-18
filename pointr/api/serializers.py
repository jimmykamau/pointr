from api.models import Points
from api.utils import find_closest_points
from rest_framework import serializers


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = "__all__"

    def create(self, validated_data):
        input_points = validated_data.get("points_list")
        points_instance, created = Points.objects.get_or_create(
            points_list=input_points
        )
        if not created:
            return points_instance

        points_list = []
        for point_str in input_points.split(";"):
            x, y = map(int, point_str.split(","))
            points_list.append((x, y))

        closest_points = find_closest_points(points_list)
        closest_points_str = ";".join(
            [f"{point[0]},{point[1]}" for point in closest_points]
        )

        points_instance.closest_points = closest_points_str
        points_instance.save()
        return points_instance
