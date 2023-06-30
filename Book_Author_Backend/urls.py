from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Book_Author_APIS.views import (
    BookListCreateView,
    BookRetrieveUpdateDeleteView,
    PageListCreateView,
    PageRetrieveUpdateDeleteView,
    UserRegisterView, UserListAPIView, BookPagesAPIView, IsAuthorAPIView,
)

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('is_author/', IsAuthorAPIView.as_view(), name='is_author'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book_retrieve_update_delete'),
    path('books/<int:bookid>/pages/', BookPagesAPIView.as_view(), name='book_pages'),
    path('pages/', PageListCreateView.as_view(), name='page_list_create'),
    path('pages/<int:pk>/', PageRetrieveUpdateDeleteView.as_view(), name='page_retrieve_update_delete'),
]
