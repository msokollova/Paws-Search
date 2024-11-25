from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from pawssearch.main.forms import CommentForm
from pawssearch.main.models import Follow, Comment
from pawssearch.posts.models import Posts


def index(request):
    return render(request, 'index.html')


class FollowedPostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'accounts/followed_posts.html'
    context_object_name = 'followed_posts'

    def get_queryset(self):
        user = self.request.user
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


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Posts.objects.get(pk=post_id)
            comment.user = request.user
            comment.save()
            return JsonResponse({
                'success': True,
                'username': request.user.username,
                'pub_date': comment.pub_date.strftime('%d %b, %Y'),
                'comment': comment.comment
            })
        return JsonResponse({'success': False})


def delete_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, post__pk=post_pk)
    post = comment.post
    if post.user == request.user:
        comment.delete()
        return redirect('detail post', pk=post.pk)
    return redirect('detail post', pk=post.pk)


@login_required
def submit_testimonial(request):
    if request.method == 'POST':
        testimonial = request.POST.get('testimonial', '')
        user_email = request.user.email
        if user_email:
            email = EmailMessage(
                subject='New User Opinion',
                body=testimonial,
                from_email=user_email,
                to=['mimsun2@gmail.com'],
                reply_to=[user_email],
            )
            email.send(fail_silently=False)
        return redirect('index')
    return redirect('index')


def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if email and message:
            full_message = f"Message from: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            send_mail(
                subject="Contact Us - Inquiry",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['mimsun2@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Вашето съобщение е изпратено успешно!")
            return redirect('contact')
        else:
            messages.error(request, "Моля, попълнете всички задължителни полета.")
    return render(request, 'contact.html')
