from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pawssearch.main.urls')),
    path('accounts/', include('pawssearch.accounts.urls')),
    path('articles/', include('pawssearch.articles.urls')),
    path('posts/', include('pawssearch.posts.urls')),
    path('donations/', include('pawssearch.donations.urls')),

]
