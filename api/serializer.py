from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    face = serializers.CharField(max_length=10)
    start = serializers.CharField(max_length=10)
    last_position = serializers.CharField(max_length=10)

    class Meta:
        model = Position
        field = ('x', 'y', 'face', 'start', 'last_position')
