from django import forms
from .models import BlogPost
class PostForm(forms.ModelForm):
    """Form for create a new  blog"""
    class Meta:
        model = BlogPost
        title = ['text']
        text = ['text']
        labels = {'text': ''}
        fields = ['title', 'text']
