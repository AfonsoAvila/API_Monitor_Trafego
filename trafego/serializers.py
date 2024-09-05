#--------------------# CREATE THE SERIALIZERS #--------------------#
#ORGANIZING THE VARIABLES

from rest_framework import serializers
from .models import SegEstrada

class SegEstradaSerializer(serializers.ModelSerializer):
    intensity = serializers.SerializerMethodField()

    class Meta:
        model = SegEstrada
        fields = ['id', 'long_start', 'lat_start', 'long_end', 'lat_end', 'length', 'speed', 'tempo_reg', 'intensity']

#DEFINE INTERVALS OF TRAFFIC INTENSITY

    def get_intensity(self, obj):
        if obj.speed > 50:
            return 'low'
        elif 20 < obj.speed <= 50:
            return 'medium'
        else:
            return 'high'
