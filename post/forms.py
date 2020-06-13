from django import forms
from django.forms import TextInput, FileInput

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail', )

        widgets = {
            'title': TextInput(attrs={'class': 'form-control mb-4'}),
            'content': TextInput(attrs={'class': 'form-control mb-4'}),
            # 'thumbnail': FileInput(attrs={'class': 'mb-4'}),
        }
