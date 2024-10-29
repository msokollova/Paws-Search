from datetime import date

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from enum import Enum

UserModel = get_user_model()


def iban_validator(value):
    if len(value) != 22 or not value.startswith("BG"):
        raise ValidationError("IBAN трябва да започва с 'BG' и да е точно 22 символа.")
    rearranged_iban = value[4:] + value[:4]
    numeric_iban = ''.join(str(int(char, 36)) if char.isalpha() else char for char in rearranged_iban)
    if int(numeric_iban) % 97 != 1:
        raise ValidationError("Невалиден IBAN.")
    return True


class Organizers(Enum):
    FOUNDATION = 'Фондация'
    INDIVIDUAL = 'Частно лице'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Donation(models.Model):

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField(
    )

    organizer = models.CharField(
        max_length=100,
        choices=Organizers.choices(),
    )

    to_date = models.DateField(
    )

    iban = models.CharField(
        max_length=22,
        validators=[
            iban_validator
        ],
    )

    pub_date = models.DateField(
        auto_now_add=True,
    )

    target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    contact_info = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    @property
    def is_expired(self):
        return self.to_date < date.today()

    def __str__(self):
        return self.title
