from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import CreateView

from .forms import PostForm
from .models import Posts, Pets, PostTypes, Regions
from ..main.forms import CommentForm
from ..main.models import Comment, Follow


class PostCreateView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('user posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('user posts')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user != request.user and not request.user.is_superuser:
            return redirect('user posts')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        is_active = self.request.POST.get('is_active') == 'True'
        form.instance.is_active = is_active
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user

        context['comments'] = Comment.objects.filter(post=post).order_by('-pub_date')
        context['follower_count'] = Follow.objects.filter(post=post).count()
        context['form'] = CommentForm()
        context['is_post_author'] = post.user == user
        context['is_following'] = Follow.objects.filter(user=user, post=post).exists()

        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return redirect('detail post', pk=post.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('user posts')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user != request.user and not request.user.is_superuser:
            return redirect('user posts')
        return super().dispatch(request, *args, **kwargs)


class UserPostsView(ListView):
    model = Posts
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user).order_by('-pub_date')


class FollowedPostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'posts/followed_posts.html'
    context_object_name = 'followed_posts'

    def get_queryset(self):
        user = self.request.user
        return Posts.objects.filter(follow__user=user, is_active=True).distinct()


class AllActivePostsView(ListView):
    model = Posts
    template_name = 'posts/all_active_posts.html'
    context_object_name = 'active_posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = Posts.objects.filter(is_active=True).order_by('-pub_date')

        # Capture filter parameters
        pet_type = self.request.GET.get('pet_type')
        post_type = self.request.GET.get('post_type')
        region = self.request.GET.get('region')

        # Apply filters based on parameters
        if pet_type:
            queryset = queryset.filter(pet_type=pet_type)
        if post_type:
            queryset = queryset.filter(post_type=post_type)
        if region:
            queryset = queryset.filter(region=region)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Providing choices to the context
        context['pet_types'] = Pets.choices()
        context['post_types'] = PostTypes.choices()
        context['regions'] = Regions.choices()

        # Current selections
        context['current_pet_type'] = self.request.GET.get('pet_type', '')
        context['current_post_type'] = self.request.GET.get('post_type', '')
        context['current_region'] = self.request.GET.get('region', '')

        return context
