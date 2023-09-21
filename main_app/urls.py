from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.BooksList.as_view(), name='index'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='detail'),
    path('books/add/', views.BookAdd.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', views.BookEdit.as_view(), name='book_edit'),
    path('books/<int:pk>/remove/', views.BookRemove.as_view(), name='book_remove'),
]