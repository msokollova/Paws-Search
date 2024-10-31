from django import forms

from pawssearch.donations.models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['title', 'description', 'organizer', 'to_date', 'target_amount', 'contact_info', 'iban']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Заглавие на каузата за дарение'}),
            'description': forms.Textarea(attrs={'class': 'w3-input', 'placeholder': 'Описание на каузата'}),
            'organizer': forms.Select(attrs={'class': 'w3-select'}),
            'iban': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете валиден IBAN'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class': 'w3-input'}),
            'target_amount': forms.NumberInput(attrs={'class': 'w3-input', 'placeholder': 'Необходима сума'}),
            'contact_info': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Телефон за връзка'}),
        }

