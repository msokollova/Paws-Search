from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    url = models.URLField(
        null=False,
        blank=False,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='static/article/images/'
    )

    pub_date = models.DateField(
        auto_now=True,
    )

