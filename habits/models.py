import datetime

from django.db import models
from django.utils.timezone import localtime

from users.models import User


def current_time():
    return localtime().time()


class Habit(models.Model):
    """Модель Привычка."""

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Создатель привычки",
        null=True,
        blank=True,
        help_text="Укажите создателя привычки",
    )
    place = models.CharField(
        max_length=50,
        verbose_name="Место",
        null=True,
        blank=True,
        help_text="Укажите место, в котором необходимо выполнить привычку",
    )
    time = models.TimeField(
        default=current_time,
        verbose_name="Время",
        help_text="Укажите время, когда необходимо выполнить привычку",
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    sign_of_pleasant_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Укажите, является ли эта привычка приятной",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Укажите привычку, которая связанная с ПОЛЕЗНОЙ привычкой",
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        null=True,
        blank=True,
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения привычки в днях",
    )
    award = models.TextField(
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение после выполнения",
    )
    time_to_complete = models.DurationField(
        default=datetime.timedelta(minutes=1),
        verbose_name="Время на выполнение",
        help_text="Укажите предположительное время на выполнение привычки",
    )
    sign_of_publicity = models.BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Укажите, можно ли публиковать привычки в общий доступ",
    )

    def __str__(self):
        return f"Привычка {self.action} пользователя {self.user}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
