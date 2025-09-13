from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import Validator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["user"]

    def validate(self, attrs):
        validator = Validator()
        validator(attrs)
        return super().validate(attrs)
