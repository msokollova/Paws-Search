from django.urls import path

from pawssearch.articles import views

urlpatterns = [
    path('', views.article_list, name='all article'),
    path('add/', views.article_add, name='add article'),
    path('<int:pk>/edit/', views.article_edit, name='edit article'),
    path('<int:pk>/delete/', views.article_delete, name='delete article'),
]
