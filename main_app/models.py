from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.title} - {self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
class Quote(models.Model):
    text = models.TextField(
        'Quote Text',
        max_length=300
        )
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f'{self.text}'