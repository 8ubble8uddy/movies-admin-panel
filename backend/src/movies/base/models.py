import uuid

from django.db import models


class TimeStampedMixin(models.Model):
    """Абстрактная модель для отметки времени."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Метаданные."""

        abstract = True


class UUIDMixin(models.Model):
    """Абстрактная модель для генерации первичных ключей."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Метаданные."""

        abstract = True


class FilmworkM2M(UUIDMixin, TimeStampedMixin):
    """Абстрактная модель для связей кинопроизведений с другими объектами."""

    film_work = models.ForeignKey(
        'movies.Filmwork',
        on_delete=models.CASCADE,
        related_name='%(class)s',
    )
    modified = None

    class Meta:
        """Метаданные."""

        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=['film_work', 'related_obj'],
                name='unique_%(app_label)s_%(class)s',
            ),
        ]
        indexes = [
            models.Index(
                fields=['film_work', 'related_obj'],
                name='%(app_label)s_%(class)s_idx',
            ),
        ]
