from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=50)
    description = models.TextField()

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    