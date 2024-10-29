from django.urls import path
from .views import DonationListView, DonationCreateView, DonationUpdateView, DonationDeleteView

urlpatterns = [
    path('', DonationListView.as_view(), name='all donations'),
    path('create/', DonationCreateView.as_view(), name='add donation'),
    path('<int:pk>/edit/', DonationUpdateView.as_view(), name='edit donation'),
    path('<int:pk>/delete/', DonationDeleteView.as_view(), name='delete donation'),
]
