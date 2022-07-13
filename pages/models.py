from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    cover = models.ImageField(upload_to='covers/')
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite', blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name='book_likes', blank=True)

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
