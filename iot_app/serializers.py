from rest_framework import serializers
from .models import Sensor, SensorData

class SensorSerializer(serializers.ModelSerializer):
    """ 
    This Serializer gives list of all Sensors
    """
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    """ 
    This Serializer gives list of all Sensors Data
    """
    class Meta:
        model = SensorData
        fields = ['sensor','value','timestamp']
        
        def get_sensor(self, obj):
          return obj.sensor.name if obj.sensor else None

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['sensor'] = SensorSerializer(instance.sensor).data
            return representation
        
class SensorDataCreateSerializer(serializers.ModelSerializer):
    """ 
    This Serializer used to create sensor data with particular sensor type
    """
    class Meta:
        model = SensorData
        exclude = ['timestamp']