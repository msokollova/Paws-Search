from django import forms
from pawssearch.posts.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'description', 'pet_type', 'post_type', 'contact_info', 'image', 'region')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Заглавие на публикацията'}),
            'description': forms.Textarea(attrs={'class': 'w3-input', 'placeholder': 'Описание на публикацията'}),
            'pet_type': forms.Select(attrs={'class': 'w3-select'}),
            'post_type': forms.Select(attrs={'class': 'w3-select'}),
            'contact_info': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Телефон за връзка (не е задължително)'}),
            'image': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'URL на снимка (не е задължително)'}),
            'region': forms.Select(attrs={'class': 'w3-select'}),
            'is_active': forms.Select(attrs={'class': 'w3-select'})
        }
