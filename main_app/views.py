from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Genre
from .forms import QuoteForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id = book_id)
    quote_form = QuoteForm()
    genre_list = book.genres.all().values_list('id')
    not_genres = Genre.objects.exclude(id__in = genre_list)
    return render(request, 'main_app/book_detail.html',{
        'book': book,
        'quote_form': quote_form,
        'not_genres': not_genres,
    })

@login_required
def books_index(request):
  books = Book.objects.filter(user=request.user)
  return render(request, 'main_app/book_list.html', {
    'books': books
  })


class BookAdd(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title','author','year','description']
    def form_valid(self,form):
       form.instance.user = self.request.user
       return super().form_valid(form)


class BookEdit(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['description']


class BookRemove(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books'

@login_required
def add_quote(request, book_id):
    form = QuoteForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.book_id = book_id
        new_form.save()
    return redirect('detail', book_id = book_id)

@login_required
def assoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.add(genre_id)
    return redirect('detail', book_id=book_id)

@login_required
def unassoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.remove(genre_id)
    return redirect('detail', book_id=book_id)


class GenreList(LoginRequiredMixin, ListView):
  model = Genre


class GenreDetail(LoginRequiredMixin, DetailView):
  model = Genre


class GenreCreate(LoginRequiredMixin, CreateView):
  model = Genre
  fields = '__all__'


class GenreUpdate(LoginRequiredMixin, UpdateView):
  model = Genre
  fields = '__all__'


class GenreDelete(LoginRequiredMixin, DeleteView):
  model = Genre
  success_url = '/genres'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect ('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
