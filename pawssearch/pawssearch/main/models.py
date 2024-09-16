from django.contrib.auth import get_user_model
from django.db import models

from pawssearch.posts.models import Posts

UserModel = get_user_model()


class Comment(models.Model):
    comment = models.TextField(
        max_length=300,
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE
    )

    followed_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'post')  # Prevent the user from following the same post multiple times


class Meta:
    ordering = ('-date_time_of_publication',)


