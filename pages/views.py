from django.shortcuts import render
from .models import Book
from django.views import generic


class BookList(generic.ListView):
    model = Book
    template_name = 'pages/home.html'
    context_object_name = 'books'
    paginate_by = 4
