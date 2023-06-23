from rest_framework.permissions import BasePermission


class AuthorPermission(BasePermission):
    def has_permission(self, request, view):
        # Allow all users to read (GET) requests
        if request.method in ['GET']:
            return True
        # Check if the user is an author for other operations
        return request.user.is_authenticated and request.user.author

    def has_object_permission(self, request, view, obj):
        # Allow authors to edit their own books and pages
        return obj.author.user == request.user


class IsAuthenticatedOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow registration (POST) and read (GET) requests without authentication
        if request.method in ['POST', 'GET']:
            return True
        # Allow authenticated users for other operations
        return request.user.is_authenticated
