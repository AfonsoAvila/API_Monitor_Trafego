#--------------------# CREATE THE MODEL #--------------------#

from django.db import models

class SegEstrada(models.Model):
    id = models.IntegerField(primary_key=True)
    long_start, lat_start, long_end, lat_end, length, speed = [models.FloatField() for _ in range(6)] #AS PER THE DATASET TO BE READ
    tempo_reg = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)

    #TO BE SEEN AS A ADMIN:
    def __str__(self):
        return f"Segment {self.id}: ({self.long_start}, {self.lat_start}) to ({self.long_end}, {self.lat_end}) with speed {self.speed} km/h"
