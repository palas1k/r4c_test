from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from robots.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"])

    class Meta:
        model = Robot
        fields = ['id', 'model', 'version', 'created']

    def validate_model(self, value):
        try:
            Robot.objects.get(model=value)
        except ValidationError:
            raise serializers.ValidationError("Такой модели робота не существует")
        return value
