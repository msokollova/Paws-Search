from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import CreateView

from .forms import PostForm
from .models import Posts
from ..main.forms import CommentForm
from ..main.models import Comment, Follow


class PostCreateView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('user posts')  # Redirect to index page after successful post creation

    def form_valid(self, form):
        # Assign the logged-in user as the author of the post
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('user posts')


class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-pub_date')
        context['follower_count'] = Follow.objects.filter(post=self.object).count()
        return context


class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('user posts')


class UserPostsView(ListView):
    model = Posts
    template_name = 'posts/user_posts.html'  # Replace with your actual template name
    context_object_name = 'posts'
    paginate_by = 10

    # Sorting by publication date in reverse order (latest post first)
    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user).order_by('-pub_date')