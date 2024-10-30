from django.contrib import admin

from pawssearch.posts.models import Posts


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'contact_info', 'region', 'pub_date', 'is_active')
    list_filter = ('pet_type', 'post_type', 'region', ('user', admin.RelatedOnlyFieldListFilter))
    search_fields = ('title',)
    search_help_text = 'Search by Title'
