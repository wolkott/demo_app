from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Author, Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'list_books.html'


class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'list_authors.html'


class CreateAuthorView(CreateView):
    model = Author
    fields = ['name', 'address', 'url']
    template_name = 'add_author.html'

    def get_form(self, form_class=None):
        form = super(CreateAuthorView, self).get_form(form_class)

        for visible in form.visible_fields():
            visible.field.widget.attrs.update({'class': 'col-sm-3'})
        return form
