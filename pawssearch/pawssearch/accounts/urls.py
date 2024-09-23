from django.contrib.auth.views import LogoutView
from django.urls import path, include

from pawssearch.accounts import views
from pawssearch.accounts.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', include([
        path('change_password', views.PasswordChangeView.as_view(), name='change_password'),
        path('delete_profile/', views.DeleteProfileView.as_view(), name='delete_profile'),

    ])),

]
