from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_related_book(self):
        return reverse('category', args=[self.id])


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category' , verbose_name=_('genre'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    author = models.CharField(max_length=50, verbose_name=_('author'))
    text = models.TextField(verbose_name=_('text'))
    price = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('price'))
    cover = models.ImageField(upload_to='covers/', verbose_name=_('cover'))
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite', blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name='book_likes', blank=True)
    views = models.IntegerField(default=0)

    create_datetime = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.id])

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
