from django import forms
from pawssearch.posts.models import Posts


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'description', 'pet_type', 'post_type', 'contact_info', 'image', 'region')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Enter post title'}),
            'description': forms.Textarea(attrs={'class': 'w3-input', 'placeholder': 'Enter description'}),
            'pet_type': forms.Select(attrs={'class': 'w3-select'}),
            'post_type': forms.Select(attrs={'class': 'w3-select'}),
            'contact_info': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Enter contact info (optional)'}),
            'image': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'Image URL (optional)'}),
            'region': forms.Select(attrs={'class': 'w3-select'}),
        }
