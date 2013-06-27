from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Street(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
