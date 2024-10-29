from django import forms

from pawssearch.donations.models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['title', 'description', 'organizer', 'to_date', 'target_amount', 'contact_info', 'iban']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Enter donation title'}),
            'description': forms.Textarea(attrs={'class': 'w3-input', 'placeholder': 'Enter donation description'}),
            'organizer': forms.Select(attrs={'class': 'w3-select'}),
            'iban': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Enter valid IBAN'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class': 'w3-input'}),
            'target_amount': forms.NumberInput(attrs={'class': 'w3-input', 'placeholder': 'Target Amount'}),
            'contact_info': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Contact Info'}),
        }

