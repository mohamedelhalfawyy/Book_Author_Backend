from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Book, Page, Author

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'book', 'content']
        read_only_fields = ['book']

    def update(self, instance, validated_data):
        # Allow authors to update the page content
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)  # Include the author serializer

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages', 'readers']
        read_only_fields = ['author', 'readers']

    def update(self, instance, validated_data):
        # Allow authors to update the book title
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
