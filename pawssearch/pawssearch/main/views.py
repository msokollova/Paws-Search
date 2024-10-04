from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from pawssearch.main.models import Follow, Comment
from pawssearch.posts.models import Posts


def index(request):
    return render(request, 'index.html')


class FollowedPostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'accounts/followed_posts.html'  # Create this template
    context_object_name = 'followed_posts'

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        # Return posts that are followed by the user and are active
        return Posts.objects.filter(follow__user=user, is_active=True).distinct()


class FollowPostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        follow, created = Follow.objects.get_or_create(user=request.user, post=post)

        if created:
            return JsonResponse({'status': 'followed'})
        else:
            return JsonResponse({'status': 'already_followed'})


class UnfollowPostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        follow = Follow.objects.filter(user=request.user, post=post)

        if follow.exists():
            follow.delete()
            return JsonResponse({'status': 'unfollowed'})
        else:
            return JsonResponse({'status': 'not_following'})


def delete_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, post__pk=post_pk)
    post = comment.post

    if post.user == request.user:
        comment.delete()
        return redirect('detail post', pk=post.pk)

    return redirect('detail post', pk=post.pk)
