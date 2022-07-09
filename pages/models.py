from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    cover = models.ImageField(upload_to='media/covers/')
    create_datetime = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
