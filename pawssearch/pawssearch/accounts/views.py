from django.contrib.auth import views as auth_views, get_user_model, login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import ListView

from pawssearch.accounts.forms import RegistrationForm, LogInForm, EditProfileForm, PasswordChangeForm
from pawssearch.main.models import Follow
from pawssearch.posts.models import Posts

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
    success_url = reverse_lazy('index')  # Redirect after successful login

    def form_invalid(self, form):
        print(form.errors)
        # Handle form validation errors here
        return super().form_invalid(form)


class EditProfileView(views.UpdateView):
    template_name = 'accounts/edit_profile.html'
    model = UserModel
    form_class = EditProfileForm
    success_url = reverse_lazy('index')


class DeleteProfileView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('index')


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    model = UserModel
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('password change done')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class FollowedPostsListView(LoginRequiredMixin, ListView):
    model = Follow
    template_name = 'accounts/followed_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Return all posts followed by the logged-in user
        return Follow.objects.filter(user=self.request.user).select_related('post')


def user_posts(request):
    all_posts = Posts.objects.filter(user=request.user).order_by('pub_date')
    paginator = Paginator(all_posts, per_page=5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'accounts/user_posts.html', context)


class LogoutView:
    pass
