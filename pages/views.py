from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
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
    is_favorite = False
    if book.favorite.filter(id=request.user.id).exists():
        is_favorite = True
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

    return render(request, 'pages/detail_page.html',
                  {'book': book, 'comments': comment, 'comment_form': comment_form, 'is_favorite': is_favorite})


def favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)

    else:
        book.favorite.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def favorite_list(request):
    user = request.user
    favorite_books = user.favorite.all()
    return render(request, 'pages/favorite_list.html', {'favorite_books': favorite_books})


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book = Book.objects.filter(title__contains=searched)
        return render(request, 'pages/search.html', {'searched': searched, 'books': book})
    else:
        return render(request, 'pages/search.html')
