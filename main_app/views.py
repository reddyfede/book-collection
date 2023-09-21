from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BooksList(ListView):
    model = Book
    fields = '__all__'

class BookDetail(DetailView):
    model = Book
    fields = '__all__'

class BookAdd(CreateView):
    model = Book
    fields = '__all__'

class BookEdit(UpdateView):
    model = Book
    fields = ['description']

class BookRemove(DeleteView):
    model = Book
    success_url = '/books'