from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instaces_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instaces_available': num_instaces_available,
                                                  'num_authors': num_authors,
                                                  },)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book