from enum import Enum
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import models

UserModel = get_user_model()


def image_url_validator(value):
    if value:
        url_validator = URLValidator(schemes=['http', 'https'])
        try:
            url_validator(value)
        except ValidationError:
            raise ValidationError(_('Enter a valid URL starting with "http://" or "https://".'), code='invalid_url')


class Pets(Enum):
    CAT = 'Котка'
    DOG = 'Куче'
    OTHER = 'Друго'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class PostTypes(Enum):
    FOUND = 'Намерено'
    MISSING = 'Изгубено'
    FOR_ADOPTION = 'За осиновяване'
    FOR_SELLING = 'За продажба'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Regions(Enum):
    BLAGOEVGRAD = 'Благоевград'
    BURGAS = 'Бургас'
    VARNA = 'Варна'
    VELIKO_TARNOVO = 'Велико Търново'
    VIDIN = 'Видин'
    VRATSA = 'Враца'
    GABROVO = 'Габрово'
    DOBRICH = 'Добрич'
    KARDZHALI = 'Кърджали'
    KYUSTENDIL = 'Кюстендил'
    LOVECH = 'Ловеч'
    MONTANA = 'Монтана'
    PAZARDZHIK = 'Пазарджик'
    PERNIK = 'Перник'
    PLEVEN = 'Плевен'
    PLOVDIV = 'Пловдив'
    RAZGRAD = 'Разград'
    RUSSE = 'Русе'
    SILISTRA = 'Силистра'
    SLIVEN = 'Сливен'
    SMOLYAN = 'Смолян'
    SOFIA = 'София - град'
    SOFIA_OBLAST = 'София - регион'
    STARA_ZAGORA = 'Стара Загарора'
    TARGOVISHTE = 'Търговище'
    HASKOVO = 'Хасково'
    SHUMEN = 'Шумен'
    YAMBOL = 'Ямбол'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Posts(models.Model):

    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    pet_type = models.CharField(
        max_length=100,
        choices=Pets.choices(),
        null=False,
        blank=False,
    )

    post_type = models.CharField(
        max_length=100,
        choices=PostTypes.choices(),
        null=False,
        blank=False,
    )

    contact_info = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=True,
        blank=True,
        validators=[
            image_url_validator,
        ]
    )

    region = models.CharField(
        max_length=200,
        choices=Regions.choices(),
        null=False,
        blank=False,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
