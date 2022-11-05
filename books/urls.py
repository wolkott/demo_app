from django import views
from django.contrib import admin
from django.urls import path
from .views import AuthorListView,HomePageView,BookListView,AuthorUpdateView,BookUpdateView,BookCreateView,AuthorCreateView,deleteBook,deleteAuthor,successPage,AuthorDeleteView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home'),
    path('books',BookListView.as_view(),name='book_list'),
    path('book',BookCreateView.as_view(),name='add_book'),
    path('book-update/<int:pk>', BookUpdateView.as_view()),
    path('delete-book/<int:id>',deleteBook),
    path('authors',AuthorListView.as_view(),name='author_list'),
    path('author',AuthorCreateView.as_view(),name='add_author'),
    path('author-update/<int:pk>', AuthorUpdateView.as_view()),
    path('delete-author/<int:pk>',AuthorDeleteView.as_view()),
    path('success',successPage),

]
