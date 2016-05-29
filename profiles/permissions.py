from rest_framework import permissions


class ProfilePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method == 'POST' or request.user.is_authenticated()
        )