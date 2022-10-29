from django import views
from django.contrib import admin
from django.urls import path
from .views import AuthorListView,HomePageView,BookListView,CreateAuthorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home'),
    path('books',BookListView.as_view(),name='book_list'),
    path('authors',AuthorListView.as_view(),name='author_list'),
    path('add_author',CreateAuthorView.as_view(),name='add_author')
]
