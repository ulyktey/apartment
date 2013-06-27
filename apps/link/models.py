from django.db import models
from apps.apartment.models import TypePoster

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Url(models.Model):
    name = models.CharField(max_length=255)
    type_url = models.ForeignKey(TypePoster)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name

