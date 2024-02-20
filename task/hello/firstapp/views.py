from django.http import *
from django.shortcuts import render

def index(request):   
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request, 'firstapp/index.html', context={'cat':cat})

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')