from rest_framework.serializers import ValidationError


class Validator:
    def __call__(self, attrs):
        related_habit = attrs.get("related_habit")
        award = attrs.get("award")
        time_to_complete = attrs.get("time_to_complete")
        sign_of_pleasant_habit = attrs.get("sign_of_pleasant_habit")
        periodicity = attrs.get("periodicity")

        if related_habit is not None and award is not None:
            raise ValidationError(
                "Невозможно одновременно задать связанную привычку и вознаграждение!"
            )
        if time_to_complete and time_to_complete.total_seconds() > 120:
            raise ValidationError("Время выполнения не должно быть больше 120 секунд!")
        if related_habit and not related_habit.sign_of_pleasant_habit:
            raise ValidationError(
                "В связанные привычки могут попадать только приятные привычки"
            )
        if sign_of_pleasant_habit and (award is not None or related_habit is not None):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки!"
            )
        if periodicity is not None and periodicity > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней!")
