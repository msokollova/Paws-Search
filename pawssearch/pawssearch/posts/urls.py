from django.urls import path

from pawssearch.posts.views import PostCreateView, PostDetailView, UserPostsView, PostEditView, PostDeleteView

urlpatterns = [
    path('create-post/', PostCreateView.as_view(), name='create post'),
    path('my-posts/', UserPostsView.as_view(), name='user posts'),  # List view of user's posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail post'),  # View details of a post
    path('edit/<int:pk>/', PostEditView.as_view(), name='edit post'),  # Edit a post
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete post'),  # Delete a post

]
