from django.http import *
from django.shortcuts import render
from .forms import UserForm

def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h1>Name entered correct</h1> {name}')
        
    return render(request, 'firstapp/index.html', context={"form": userform})

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')