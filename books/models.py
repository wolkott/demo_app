from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    @property
    def authorName(self):
        return self.author.name


    @property
    def authorId(self):
        return self.author.id
