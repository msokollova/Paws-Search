from django import forms

from pawssearch.main.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'w3-input', 'placeholder': 'Добавете коментар...', 'rows': 3}),
        }
