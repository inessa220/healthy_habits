from django_celery_beat.utils import now_localtime

from config.celery import shared_task
from habits.models import Habit
from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_inform_habit(email):
    """Отправляется сообщение пользователю, что необходимо выполнить привычку."""
    message = "Необходимо выполнить привычку"
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        send_telegram_message(user.tg_chat_id, message)


@shared_task()
def is_active_habit():
    habits = Habit.objects.filter(user__isnull=False, time_lead=now_localtime)
    for habit in habits:
        send_inform_habit.delay(habit.user.email)
