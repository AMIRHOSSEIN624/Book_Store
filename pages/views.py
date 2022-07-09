from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views import generic
from .forms import CommentForm


class BookList(generic.ListView):
    model = Book
    template_name = 'pages/home.html'
    context_object_name = 'books'
    paginate_by = 4


def detail_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comment = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'pages/detail_page.html', {'book': book, 'comments': comment,'comment_form':comment_form})
