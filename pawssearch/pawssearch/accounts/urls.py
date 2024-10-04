from django.contrib.auth.views import LogoutView
from django.urls import path, include

from pawssearch.accounts import views
from pawssearch.accounts.views import LoginView
from pawssearch.main.views import FollowedPostsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('change_password_done/', views.PasswordChangeDoneView.as_view(), name='password change done'),
    path('my-followed-posts/', FollowedPostsView.as_view(), name='followed posts'),
    path('profile/<int:pk>/', include([
        path('change_password', views.PasswordChangeView.as_view(), name='change password'),
        path('delete_profile/', views.DeleteProfileView.as_view(), name='delete profile'),
        path('edit_profile/', views.EditProfileView.as_view(), name='edit profile'),
        path('change_password/', views.PasswordChangeView.as_view(), name='change password'),
    ])),

]
