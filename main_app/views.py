from django.shortcuts import render
from .models import Book

# Create your views here.

# books = [
#     {'title': 'Moby Dick', 'author': 'Herman Melville', 'year':1851, 'description':'A book about an old man that likes fishing.'},
#     {'title': 'Frankestein', 'author': 'Mary Shelley', 'year':1818, 'description':'A book about a monster not called Frankestein.'},
#     {'title': 'Dracula', 'author': 'Bram Stoker', 'year':1897, 'description':'There\'s almost no Dracula in here.'},
#     {'title': 'The Colour Out of Space', 'author': 'H.P. Lovecraft', 'year':1927, 'description':'A short story about color blindness.'},
# ]

# b = Book(title= 'Moby Dick',author= 'Herman Melville', year=1851, description='A book about an old man that likes fishing.')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })