from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """Check if user is active"""

    def has_permission(self, request, view):
        if not request.user.is_superuser:
            return False
        return True

