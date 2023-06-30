from rest_framework import generics, permissions
from .models import Book, Page, User, Author
from .serializers import BookSerializer, PageSerializer, UserSerializer, AuthorSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is authenticated and has an associated Author object
        if request.user.is_authenticated:
            author = Author.objects.filter(user=request.user).first()
            return author is not None

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions for updating page content
        if request.user.is_authenticated and isinstance(obj, Page):
            return obj.book.author.user == request.user

        # Allow write permissions only if the user is authenticated and the author is associated
        if request.user.is_authenticated and hasattr(obj, 'author'):
            return obj.author.user == request.user

        return False


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class IsAuthorAPIView(APIView):
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request):
        # The permission class will handle the authorization check
        # If the user is not an author, it will raise a permission denied exception
        author = request.user.author
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookPagesAPIView(generics.ListAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        book_id = self.kwargs['bookid']
        return Page.objects.filter(book_id=book_id)


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]


class PageListCreateView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthorOrReadOnly]
