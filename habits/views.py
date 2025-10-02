from django.shortcuts import get_object_or_404
from django_celery_beat.utils import now_localtime
from rest_framework.decorators import action
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from habits.tasks import send_inform_habit
from users.permissions import IsOwner


class UserHabitViewSet(ModelViewSet):
    """Полный цикл CRUD операций. Возвращает список только публичных привычек."""

    queryset = Habit.objects.filter(sign_of_publicity=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPagination

    @action(methods=["get"], detail=True)
    def time_lead(self, request, pk=None):
        habit = get_object_or_404(Habit, pk=pk)
        if habit.time_lead.filter(pk=request.user.pk) == now_localtime:
            send_inform_habit.delay(habit.user.email)
        serializer = self.get_serializer(habit)
        return Response(data=serializer.data)


class HabitCreateApiView(CreateAPIView):
    """Создание новых привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListApiView(ListAPIView):
    """Получение списка всех привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    pagination_class = CustomPagination

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)


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
