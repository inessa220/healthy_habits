from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitRetrieveView,
                          HabitUpdateApiView, UserHabitViewSet)

app_name = HabitsConfig.name

router = SimpleRouter()
router.register("", UserHabitViewSet)

urlpatterns = [
    path("habits/", HabitListApiView.as_view(), name="habits_list"),
    path("habits/<int:pk>/", HabitRetrieveView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitCreateApiView.as_view(), name="habits_create"),
    path("habits/<int:pk>/delete", HabitDestroyApiView.as_view(), name="habits_delete"),
    path("habits/<int:pk>/update", HabitUpdateApiView.as_view(), name="habits_update"),
]

urlpatterns += router.urls
