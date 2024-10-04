from django.urls import path

from pawssearch.posts.views import PostCreateView, PostDetailView, UserPostsView, PostEditView, PostDeleteView, \
    AllActivePostsView

urlpatterns = [
    path('create-post/', PostCreateView.as_view(), name='create post'),
    path('my-posts/', UserPostsView.as_view(), name='user posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail post'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='edit post'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete post'),
    path('all-active-posts/', AllActivePostsView.as_view(), name='all active posts'),

]
