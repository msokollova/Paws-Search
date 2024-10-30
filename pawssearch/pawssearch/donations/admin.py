from django.contrib import admin

from pawssearch.donations.models import Donation


@admin.register(Donation)
class DonationModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'to_date', 'iban', 'target_amount', 'contact_info', 'description')
    list_filter = ('organizer',)
    search_fields = ('title',)
    search_help_text = 'Search by Title'
