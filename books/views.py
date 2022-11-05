from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView,DeleteView
from django.contrib import messages
from books.forms import AuthorForm, BookForm
from .models import Author, Book
from django.urls import reverse,reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'list_books.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')


def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('books')


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')



class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'list_authors.html'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_update.html'
    success_url = reverse_lazy('author_list')


def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    author.delete
    return HttpResponseRedirect(reverse_lazy('author_list'))


def successPage(request):
    context={"Action":"Data successfully processed"}
    return render(request,'success.html',context)

