from django.shortcuts import render
from .model import *

def ads(request):
    return render(request, 'ads/ads.html', {})
