from django.contrib import messages
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import ListView

from pawssearch.accounts.forms import RegistrationForm, LogInForm, EditProfileForm, PasswordChangeForm
from pawssearch.main.models import Follow

UserModel = get_user_model()


class RegisterView(views.CreateView):
    template_name = 'accounts/register_account.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginView(auth_views.LoginView):
    form_class = LogInForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, "Невалидно потребителско име или парола.")
        return super().form_invalid(form)


class EditProfileView(views.UpdateView):
    template_name = 'accounts/edit_profile.html'
    model = UserModel
    form_class = EditProfileForm
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class DeleteProfileView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return UserModel.objects.filter(pk=self.request.user.pk)


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('password change done')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class LogoutView:
    pass
