from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from pawssearch.donations.forms import DonationForm
from pawssearch.donations.models import Donation, Organizers


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class DonationListView(ListView):
    model = Donation
    template_name = 'donations/all_donations.html'
    context_object_name = 'donations'

    def get_queryset(self):
        queryset = super().get_queryset()
        organizer = self.request.GET.get('organizer')
        status = self.request.GET.get('status')
        today = timezone.now().date()

        if organizer:
            queryset = queryset.filter(organizer=organizer)

        if status == 'active':
            queryset = queryset.filter(to_date__gte=today)
        elif status == 'inactive':
            queryset = queryset.filter(to_date__lt=today)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer_choices'] = Organizers.choices()
        context['status_choices'] = [('active', 'Активна'), ('inactive', 'Неактивна')]
        context['current_organizer'] = self.request.GET.get('organizer', '')
        context['current_status'] = self.request.GET.get('status', '')
        return context


class DonationCreateView(StaffRequiredMixin, CreateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donations/donation_form.html'
    success_url = reverse_lazy('all donations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Добавяне'
        return context


class DonationUpdateView(StaffRequiredMixin, UpdateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donations/donation_form.html'
    success_url = reverse_lazy('all donations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Редактиране'
        return context


class DonationDeleteView(StaffRequiredMixin, DeleteView):
    model = Donation
    template_name = 'donations/donation_confirm_delete.html'
    success_url = reverse_lazy('all donations')
    context_object_name = 'donation'
