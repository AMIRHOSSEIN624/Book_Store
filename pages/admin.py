from django.contrib import admin
from .models import Book, Comment, Category

admin.site.register(Category)


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ('user', 'book', 'text',)
    extra = 0

admin.site.register(Comment)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'user',)
    inlines = [

        CommentInline,
    ]

