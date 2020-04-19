from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import os
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    s = "Event List"
    context = {
        's': s,
    }
    return render(request, 'index.html', context)


def notfound(request):
    return render(request, 'notfound.html')