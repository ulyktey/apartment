from django.db import models
from apps.location.models import Region, City, District, Street

class TypePoster(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Flat(models.Model):
    type_flat = models.CharField(max_length=100)
    street = models.ForeignKey(Street)
    district = models.ForeignKey(District)
    city = models.ForeignKey(City)
    region = models.ForeignKey(Region)
    room_count = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    max_floor = models.IntegerField(null=True)
    s_all = models.IntegerField(null=True)
    s_live = models.IntegerField(null=True)
    s_cook = models.IntegerField(null=True)
    price = models.CharField(max_length=100, null=True)
    price_sq_m = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    type_poster = models.ForeignKey(TypePoster)
    email = models.CharField(max_length=100, null=True)
    name_on_site = models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    phone = models.ManyToManyField(Phone)
    def __unicode__(self):
        return self.street.name + ' ' + self.district.name  + ' ' + self.city.name




class Image(models.Model):
    name = models.CharField(max_length=255)
    flat = models.ForeignKey(Flat)

    def __unicode__(self):
        return self.name

