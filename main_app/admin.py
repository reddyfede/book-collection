from django.contrib import admin
from .models import Book, Quote, Genre

# Register your models here.

admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(Genre)