from typing import Any, Dict

from django.contrib.postgres.aggregates import ArrayAgg
from django.db import models
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import Filmwork, Role


class MoviesApiMixin:
    """Базовый класс для представления кинопроизведений."""

    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self) -> QuerySet[Filmwork]:
        """Подготовляет запрос со всеми кинопроизведениями.

        - порядок по дате создании записи;
        - представление в виде словарей;
        - добавлены поля жанров и ролей участников кинопроизведения.

        Returns:
            QuerySet[Filmwork]: Кинопроизведения в виде словарей.
        """
        genres = {
            'genres': ArrayAgg(
                'genres__name',
                distinct=True,
                filter=models.Q(genrefilmwork__related_obj__name__isnull=False),
            ),
        }
        persons = {
            f'{role}s': ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=models.Q(personfilmwork__role=role),
            )
            for role, _ in Role.choices
        }
        return (
            Filmwork.objects
            .order_by('created')
            .values('id', 'title', 'description', 'creation_date', 'rating', 'type')
            .annotate(**genres, **persons)
        )

    def render_to_response(self, context: Dict[str, Any], **kwargs: Any) -> JsonResponse:
        """Форматирует данные страницы с кинопроизведениями в JSON.

        Args:
            context: Словарь страницы с кинопроизведениями;
            kwargs: Необязательные именованные аргументы.

        Returns:
            JsonResponse: Страница с кинопроизведениями в JSON.
        """
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    """Класс для отображения всех кинопроизведений."""

    paginate_by = 50

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Возвращает словарь с данными для формирования страницы с кинопроизведениями.

        Args:
            kwargs: Необязательные именованные аргументы.

        Returns:
            dict[str, any]: Словарь для постраничного отображения кинопроизведений.
        """
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by,
        )
        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    """Класс для отображения одного кинопроизведения."""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Возвращает словарь с данными для формирования страницы одного кинопроизведения.

        Args:
            kwargs: Необязательные именованные аргументы.

        Returns:
            dict[str, any]: Словарь для отображения кинопроизведения.
        """
        context = super().get_context_data()
        return context['object']
