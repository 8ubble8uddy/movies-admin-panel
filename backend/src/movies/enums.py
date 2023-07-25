from django.db import models
from django.utils.translation import gettext_lazy as _


class Type(models.TextChoices):
    """Вспомогательная модель для выбора типа кинопроизведений."""

    movie = 'movie', _('movie')
    tv_show = 'tv show', _('tv show')


class Role(models.TextChoices):
    """Вспомогательная модель для выбора ролей персон."""

    actor = 'actor', _('actor')
    director = 'director', _('director')
    writer = 'writer', _('writer')
