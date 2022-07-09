from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views import generic


class BookList(generic.ListView):
    model = Book
    template_name = 'pages/home.html'
    context_object_name = 'books'
    paginate_by = 4


def detail_page(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'pages/detail_page.html', {'book': book})
