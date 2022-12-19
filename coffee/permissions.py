from rest_framework.permissions import BasePermission, SAFE_METHODS

class OwnerOnly(BasePermission): # the owner only can edit or delete from his permission
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user