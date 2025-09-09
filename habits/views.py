from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class UserHabitViewSet(ModelViewSet):
    """Полный цикл CRUD операций. Возвращает список только публичных привычек."""

    queryset = Habit.objects.filter(sign_of_publicity=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


class HabitCreateApiView(CreateAPIView):
    """Создание новых привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListApiView(ListAPIView):
    """Получение списка всех привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    pagination_class = CustomPagination


class HabitRetrieveView(RetrieveAPIView):
    """Получение одной конкретной привычки по id."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitUpdateApiView(UpdateAPIView):
    """Обновление существующих привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyApiView(DestroyAPIView):
    """Удаление привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
