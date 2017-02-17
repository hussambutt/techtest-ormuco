from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("<h1>Still working on it</h1>")

def detail(request):
    template = loader.get_template('form/index.html')
    return HttpResponse(template.render(request))
