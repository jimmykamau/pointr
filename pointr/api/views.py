from api.models import Points
from api.serializers import PointsSerializer
from rest_framework import generics


class GetCreatePointsApiView(generics.ListCreateAPIView):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
