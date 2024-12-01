from rest_framework import permissions


class CheckCreateStore(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'владелец':
            return True
        return False


class CheckEditStore(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner