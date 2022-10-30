from django import forms
from .models import Author


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    url = forms.CharField(max_length=200)


class BookForm(forms.Form):
    title = forms.CharField(max_length=150)
    pages = forms.IntegerField
    price = forms.DecimalField(max_digits=5, decimal_places=2)
