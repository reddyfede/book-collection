from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Book
from .forms import QuoteForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_detail(request, book_id):
    book = Book.objects.get(id = book_id)
    quote_form = QuoteForm()
    return render(request, 'main_app/book_detail.html',{
        'book': book,
        'quote_form': quote_form,
    })

class BooksList(ListView):
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

def add_quote(request, book_id):
    form = QuoteForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.book_id = book_id
        new_form.save()
    return redirect('detail', book_id = book_id)
