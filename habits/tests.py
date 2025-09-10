from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тест CRUD для Привычки."""

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.habit = Habit.objects.create(user=self.user, action="Зарядка")
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habits_create")
        data = {"action": "Иностранный язык", "time_to_complete": 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        new_habit = Habit.objects.latest("pk")
        self.assertEqual(new_habit.action, data["action"])

    def test_habit_update(self):
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {"action": "Разминка"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Разминка")

    def test_habit_delete(self):
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "sign_of_pleasant_habit": self.habit.sign_of_pleasant_habit,
                    "periodicity": self.habit.periodicity,
                    "award": self.habit.award,
                    "time_to_complete": self.habit.time_to_complete,
                    "sign_of_publicity": self.habit.sign_of_publicity,
                    "user": self.user.pk,
                    "related_habit": self.habit.related_habit,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
