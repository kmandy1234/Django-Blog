# just for example. not a part of project.
from django import forms

from . models import Post

class ExamplePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
