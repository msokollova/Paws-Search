from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'url', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Enter article title'}),
            'url': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'Article URL'}),
            'image': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'Image URL (optional)'}),
        }
