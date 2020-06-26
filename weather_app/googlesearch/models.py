from django.db import models

# Create your models here.


class WEATHER_RECURRENT(models.Model):
    tentp = models.CharField(max_length=200)
    feel_like = models.FloatField(default=0)
    temp_min = models.FloatField(default=0)
    temp_max = models.FloatField(default=0)
    w_descript = models.CharField(max_length=200)
    cloud = models.FloatField(default=0)
    wind_speed = models.FloatField(default=0)

