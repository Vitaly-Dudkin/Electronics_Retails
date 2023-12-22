from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Check if user is active"""

    def has_permission(self, request, view):
        if not request.user.is_active:
            return False
        return True
