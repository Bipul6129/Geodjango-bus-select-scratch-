from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    # objects = models.GeometryCollectionField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"

    def as_dict(self):
        return{
            'markerid':self.id,
            'lon':self.location.x,
            'lat':self.location.y,
        }

class Bus(models.Model):
    location = models.PointField(srid=4326)
    yatayat = models.CharField(max_length=20)
    bus_image = models.ImageField(default='busdefault.png')

    def __str__(self):
        return self.yatayat
