from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.BooksList.as_view(), name='index'),
    path('books/<int:book_id>/', views.book_detail, name='detail'),
    path('books/add/', views.BookAdd.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', views.BookEdit.as_view(), name='book_edit'),
    path('books/<int:pk>/remove/', views.BookRemove.as_view(), name='book_remove'),
    path('books/<int:book_id>/add_quote/', views.add_quote, name='add_quote'),
    path('books/<int:book_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name='assoc_genre'),
    path('books/<int:book_id>/unassoc_genre/<int:genre_id>/', views.unassoc_genre, name='unassoc_genre'),
]