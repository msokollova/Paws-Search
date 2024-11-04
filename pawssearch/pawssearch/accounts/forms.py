from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from pawssearch.accounts.models import PawsSearchUser

UserModel = get_user_model()


class RegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = PawsSearchUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете потребителско име'}),
            'email': forms.EmailInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете email адрес'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Applying widgets from Meta to 'username' and 'email' fields
        self.fields['username'].widget.attrs.update(self.Meta.widgets['username'].attrs)
        self.fields['email'].widget.attrs.update(self.Meta.widgets['email'].attrs)

        # Manually adding widgets for 'password1' and 'password2' fields
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'w3-input', 'placeholder': 'Въведете парола'}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'w3-input', 'placeholder': 'Потвърдете паролата'}
        )


class LogInForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете Вашето потребителско име'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете Вашата парола'})
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = PawsSearchUser
        fields = ('first_name', 'last_name', 'email', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете име (не е задължително)'}),
            'last_name': forms.EmailInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете фамилия (не е задължително)'}),
            'email': forms.EmailInput(attrs={'class': 'w3-input', 'placeholder': 'Въведете email адрес'}),
            'profile_picture': forms.URLInput(attrs={'class': 'w3-input', 'placeholder': 'URL на снимка (не е задължително)'}),
        }


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = PawsSearchUser
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={'class': 'w3-input', 'placeholder': 'Въведете старата си парола'}
        )
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={'class': 'w3-input', 'placeholder': 'Въведете нова парола'}
        )
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={'class': 'w3-input', 'placeholder': 'Потвърдете новата парола'}
        )