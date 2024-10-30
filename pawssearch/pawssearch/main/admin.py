from django.contrib import admin

from pawssearch.main.models import Comment, Follow


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'pub_date', 'post_title')
    list_filter = (('user', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('post__title',)
    search_help_text = 'Search by Post Title'

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = 'Post Title'


@admin.register(Follow)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_title', 'followed_at')
    list_filter = (('user', admin.RelatedOnlyFieldListFilter),)
    search_fields = ('post__title',)

    def post_title(self, obj):
        return obj.post.title

    post_title.short_description = 'Post Title'
