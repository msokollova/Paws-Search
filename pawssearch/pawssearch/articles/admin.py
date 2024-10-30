from django.contrib import admin

from pawssearch.articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'pub_date')
    search_fields = ('title',)
    search_help_text = 'Search by Title'
