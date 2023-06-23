from rest_framework import serializers

from .models import Book, Page


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

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages']
        read_only_fields = ['author']

    def update(self, instance, validated_data):
        # Allow authors to update the book title
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        return instance
