from .models import Comment,Book
from django import forms


class FormCreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('genre', 'title', 'author', 'text', 'price', 'cover', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
