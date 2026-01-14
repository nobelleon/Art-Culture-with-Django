from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def exploration_view(request):
    exploration_view = loader.get_template('exploration.html')
    return HttpResponse(exploration_view.render())