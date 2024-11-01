from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from pawssearch.accounts.models import PawsSearchUser

UserModel = get_user_model()


class RegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = PawsSearchUser
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Потребителско име',
            }))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Парола'
            }
        )
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = PawsSearchUser
        fields = ('first_name', 'last_name', 'email', 'profile_picture')


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    pass
