from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrOwnerReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.method in SAFE_METHODS:
            return True
        return obj == request.user