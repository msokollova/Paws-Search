from django.core import validators, exceptions
from django.db import models
from django.contrib.auth import models as auth_model


def name_value_validator(value):
    if not value[0].isalpha() or not value[0].isupper():
        raise exceptions.ValidationError('Both first and last name should start with capital letter!')
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Names should contain only letters!')


class PawsSearchUser(auth_model.AbstractUser):
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 100

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="First name",
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
            name_value_validator,
        )
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Last name",
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
            name_value_validator,
        )
    )

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    @property
    def full_name(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result
