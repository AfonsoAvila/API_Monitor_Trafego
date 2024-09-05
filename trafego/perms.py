#--------------------# PERMISSIONS CLASS, EITHER STAFF (ADMIN) OR ANON #--------------------#

from rest_framework import permissions

class AdminOrAnon(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff
