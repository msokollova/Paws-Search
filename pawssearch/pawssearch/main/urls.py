from django.urls import path

from pawssearch.main import views
from pawssearch.main.views import index, FollowPostView, UnfollowPostView

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete comment'),
    path('post/<int:pk>/follow/', FollowPostView.as_view(), name='follow post'),
    path('post/<int:pk>/unfollow/', UnfollowPostView.as_view(), name='unfollow post'),
    path('submit-testimonial/', views.submit_testimonial, name='submit_testimonial'),
]
