from rest_framework import permissions


class MyIsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.methods in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class MyOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  obj.user == request.user