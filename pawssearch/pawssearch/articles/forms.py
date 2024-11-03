from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'url')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Заглавие на статията'}),
            'url': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'URL на статията'}),
        }
