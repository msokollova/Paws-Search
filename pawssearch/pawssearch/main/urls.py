from django.urls import path

from pawssearch.main.views import index

urlpatterns = [
    path('', index, name='index'),
]
