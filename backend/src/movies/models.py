from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.base.models import FilmworkM2M, TimeStampedMixin, UUIDMixin
from movies.enums import Role, Type

DEFAULT_LENGTH = 255


class Person(UUIDMixin, TimeStampedMixin):
    """Базовая модель для персон."""

    full_name = models.CharField(_('full name'), max_length=DEFAULT_LENGTH)

    class Meta:
        """Метаданные персон."""

        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self) -> str:
        """Строковое представление персоны в виде её полного имени.

        Returns:
            str: Полное имя персоны
        """
        return self.full_name


class Genre(UUIDMixin, TimeStampedMixin):
    """Базовая модель для жанров."""

    name = models.CharField(_('name'), max_length=DEFAULT_LENGTH)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        """Метаданные жанров."""

        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    def __str__(self):
        """Строковое представление жанра в виде его названия.

        Returns:
            str: Название жанра
        """
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    """Базовая модель для кинопроизведений."""

    title = models.CharField(_('title'), max_length=DEFAULT_LENGTH)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(
        _('creation date'),
        null=True,
        db_index=True,
    )
    rating = models.FloatField(
        _('rating'),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.CharField(
        _('type'),
        max_length=DEFAULT_LENGTH,
        choices=Type.choices,
    )
    genres = models.ManyToManyField(
        Genre,
        through='GenreFilmwork',
        related_name='film_works',
    )
    persons = models.ManyToManyField(
        Person,
        through='PersonFilmwork',
        related_name='film_works',
    )

    class Meta:
        """Метаданные кинопроизведений."""

        db_table = "content\".\"film_work"
        verbose_name = _('film work')
        verbose_name_plural = _('film works')

    def __str__(self):
        """Строковое представление кинопроизведения в виде его названия.

        Returns:
            str: Название кинопроизведения
        """
        return self.title


class GenreFilmwork(FilmworkM2M):
    """Промежуточная модель для кинопроизведений и жанров."""

    related_obj = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        db_column='genre_id',
        verbose_name=_('genre'),
    )

    class Meta(FilmworkM2M.Meta):
        """Метаданные жанров кинопроизведений."""

        db_table = "content\".\"genre_film_work"
        verbose_name = _('genre film work')
        verbose_name_plural = _('genres film work')


class PersonFilmwork(FilmworkM2M):
    """Промежуточная модель для кинопроизведений и персон."""

    related_obj = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id',
        verbose_name=_('person'),
    )
    role = models.CharField(
        _('role'),
        max_length=DEFAULT_LENGTH,
        choices=Role.choices,
    )

    class Meta(FilmworkM2M.Meta):
        """Метаданные персон кинопроизведений."""

        db_table = "content\".\"person_film_work"
        verbose_name = _('person film work')
        verbose_name_plural = _('persons film work')
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'related_obj', 'role'],
                name='unique_%(app_label)s_%(class)s',
            ),
        ]
