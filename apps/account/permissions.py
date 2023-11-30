from rest_framework import generics, permissions
from .models import Account


class IsClientPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.role == 2:
            return True
        else:
            return False

    def has_permission(self, request, view):
        return True



class IsOwnUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.id == request.user.id