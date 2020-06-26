from rest_framework import serializers
from .models import WEATHER_RECURRENT


class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WEATHER_RECURRENT
        fields = ('TENTP', 'FEEL_LIKE', 'TEMP_MIN', 'TEMP_MAX', 'W_DESCRIPT', 'CLOUD', 'WIND_SPEED')


