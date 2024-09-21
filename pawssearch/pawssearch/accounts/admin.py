from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'full_name', 'email')
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    search_help_text = 'Search by Email, First name or Last name'