from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    url = models.URLField(
        null=False,
        blank=False,
    )

    pub_date = models.DateField(
        auto_now=True,
    )
