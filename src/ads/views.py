from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse

def ads(request):
    return render(request, 'main/index.html', {})
