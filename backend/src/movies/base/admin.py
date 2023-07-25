from django.contrib import admin

from movies.models import GenreFilmwork, PersonFilmwork


class GenreFilmworkInline(admin.TabularInline):
    """Класс для вставки жанров в админку кинопроизведений."""

    model = GenreFilmwork
    autocomplete_fields = ('related_obj',)


class PersonFilmworkInline(admin.TabularInline):
    """Класс для вставки персон в админку кинопроизведений."""

    model = PersonFilmwork
    autocomplete_fields = ('related_obj',)
