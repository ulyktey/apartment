"""Db django orm utils
"""
from django.core.management import setup_environ
from project import settings
setup_environ(settings)

from apps.location.models import City, Region, District, Street
from apps.link.models import Url
from apps.apartment.models import Phone, Image, Flat, TypePoster
import time

def set_flat(data):
    """Set information about flat
    """
    list_phone = []
    for phone in data['phone']:
        phone_objs = get_phone(phone)
        if len(phone_objs) <= 0:
            obj = Phone(name = phone)
            obj.save()
            list_phone.append(obj)
        else:
            list_phone.append(phone_objs[0])

    flat = Flat(type_flat = data['type_room'],
                street = data['street'],
                district = data['district'],
                city = data['city'],
                region = data['region'],
                room_count = data['count_room'],
                floor = data['floor'],
                max_floor = data['max_floor'],
                s_all = data['s_live'] + data['s_cook'],
                s_live = data['s_live'],
                s_cook = data['s_cook'],
                price = data['price'],
                price_sq_m = data['full_price'],
                description = data.get('description', 'null'),
                type_poster =  data['type_poster'],
                email = data.get('email', ' '),
                name_on_site = time.time())
    flat.save()
    for i in list_phone:
        flat.phone.add(i)
    for img in data['image']:
        obj_img = Image(name = img, flat = flat)
        obj_img.save()


def get_urls():
    """Get all url

    :Return:
        urls object
    """
    try:
        return Url.objects.all()
    except Url.DoesNotExist:
        return None


def set_region_and_city(data):
    """Set data to db

    :Parameters:
        -`data`: dictionary with data region and city

    """
    for k in data.keys():
        region_data = Region(name = k)
        region_data.save()
        for val in data[k]:
            city_data = City(region = region_data, name = val)
            city_data.save()

def set_district_and_street(data, city_id):
    """Set data to db

    :Parameters:
        -`data`: dictionary with data district and street

    """
    city = get_city_by_id(city_id)
    if city is not None:
        for k in data.keys():
            district_data = District(city = city, name = k)
            district_data.save()
            for val in data[k]:
                street_data = Street(district = district_data, name = val)
                street_data.save()

def get_city(name_city):
    """Get city by name

    :Parameters:
        -`name_city`: city name

    :Return:
        city object
    """
    try:
        return City.objects.filter(name = name_city)
    except City.DoesNotExist:
        return None


def get_phone(phone):
    """Get phone by name

    :Parameters:
        -`phone`: phone name

    :Return:
        city object
    """
    try:
        return Phone.objects.filter(name = phone)
    except Phone.DoesNotExist:
        return None

def get_street(name):
    """Get street by name

    :Parameters:
        -`name`:  name

    :Return:
        street object
    """
    try:
        return Street.objects.filter(name = name)
    except Street.DoesNotExist:
        return None

def get_city_by_id(city_id):
    """Get city by id

    :Parameters:
        -`city_id`: city id

    :Return:
        city object
    """
    try:
        return City.objects.get(id = city_id)
    except City.DoesNotExist:
        return None

def get_district_by_id(district_id):
    """Get district by id

    :Parameters:
        -`city_id`: city id

    :Return:
        city object
    """
    try:
        return District.objects.get(id = district_id)
    except District.DoesNotExist:
        return None


def get_region_by_id(region_id):
    """Get region by id

    :Parameters:
        -`region_id`: region id

    :Return:
        region object
    """
    try:
        return Region.objects.get(id = region_id)
    except Region.DoesNotExist:
        return None


def get_poster_by_id(poster_id):
    """Get poster by id

    :Parameters:
        -`poster_id`: poster id

    :Return:
        poster object
    """
    try:
        return TypePoster.objects.get(id = poster_id)
    except TypePoster.DoesNotExist:
        return None

