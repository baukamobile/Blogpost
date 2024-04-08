from django import forms
from .models import Blog,Author


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'