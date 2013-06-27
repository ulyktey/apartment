from django.template.loader import get_template
from django.http import HttpResponse
from django.http import Http404
from django import template
from django.views.decorators.csrf import csrf_exempt
#import json
#import os
#import logging
#from location.models import Region, City
#import parse_content
def home(request):
    return HttpResponse('home')

