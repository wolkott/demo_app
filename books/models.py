from django.db import models
from django.urls import reverse


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=200, null=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def authorName(self):
        return self.author.name

    @property
    def authorId(self):
        return self.author.id
