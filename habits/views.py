from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.serializers import HabitSerializer


class UserHabitViewSet(ModelViewSet):
    """Полный цикл CRUD операций. Возвращает список только публичных привычек."""

    queryset = Habit.objects.filter(sign_of_publicity=True)
    serializer_class = HabitSerializer


class HabitCreateApiView(CreateAPIView):
    """Создание новых привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListApiView(ListAPIView):
    """Получение списка всех привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveView(RetrieveAPIView):
    """Получение одной конкретной привычки по id."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    """Обновление существующих привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(DestroyAPIView):
    """Удаление привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
