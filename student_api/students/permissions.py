

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    """
    Custom permission to allow only staff users to edit objects,
    while allowing read-only access to everyone.
    """

    def has_permission(self, request, view):
        # Allow read-only access for safe methods (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Allow write access only for staff users
        return request.user.is_staff