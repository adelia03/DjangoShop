from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # esli prosto chtenie
            return True
        if request.user.is_authenticated:
            return True
        
        
    # PUT, PATCH, DELETE, GET(WITH ID)
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # esli prosto chtenie
            return True
        if not request.user.is_authenticated:
            # esli usera net
            return False
        if request.user == obj.author:
            return True