from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Book, Category
from django.views import generic
from .forms import CommentForm, FormCreateBook
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class BookList(generic.ListView):
    model = Book
    template_name = 'pages/home.html'
    context_object_name = 'books'
    paginate_by = 4


def category_filter(request, pk):
    cat = Book.objects.filter(genre=pk)

    return render(request, 'pages/category.html', {'category': cat})


def like_view(request, pk):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    liked = False
    if book.likes.filter(id=request.user.id).exists():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail_page', args=[str(pk)]))


def detail_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.views += 1
    book.save()
    comment = book.comments.all()
    total_likes = book.total_likes()
    is_favorite = False
    liked = False
    if book.favorite.filter(id=request.user.id).exists():
        is_favorite = True
    if book.likes.filter(id=request.user.id).exists():
        liked = True
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
                  {'book': book, 'comments': comment, 'comment_form': comment_form, 'is_favorite': is_favorite,
                   'total_likes': total_likes, 'liked': liked, })


def favorite_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)

    else:
        book.favorite.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
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


class CreateBook(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = FormCreateBook
    template_name = 'pages/create_book.html'
    success_url = reverse_lazy('home')


class UpdateBook(UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = FormCreateBook
    template_name = 'pages/create_book.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class DeleteBook(UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'pages/delete_book.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


def filter_by(request):
    sort_by = request.GET.get('sort', 'low')
    if sort_by == 'low':
        product = Book.objects.filter().order_by('price')
    elif sort_by == 'high':
        product = Book.objects.filter().order_by('-price')
    elif sort_by == 'new':
        product = Book.objects.filter().order_by('-create_datetime')
    # elif sort_by == 'old':
    #     product = Book.objects.filter().order_by('create_datetime')
    return render(request, 'pages/filter_list.html', {'sort': sort_by, 'product': product})
