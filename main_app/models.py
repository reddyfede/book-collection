from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.title} - {self.id}'