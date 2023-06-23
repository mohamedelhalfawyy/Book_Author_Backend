"""Book_Author_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Book_Author_APIS.views import (
    BookListCreateView,
    BookRetrieveUpdateDeleteView,
    PageListCreateView,
    PageRetrieveUpdateDeleteView,
    UserRegisterView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book_retrieve_update_delete'),
    path('pages/', PageListCreateView.as_view(), name='page_list_create'),
    path('pages/<int:pk>/', PageRetrieveUpdateDeleteView.as_view(), name='page_retrieve_update_delete'),
]
