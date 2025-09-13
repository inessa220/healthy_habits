from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь создателем привычки."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
