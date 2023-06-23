from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    # Add your custom fields here
    groups = models.ManyToManyField(Group, related_name='book_author_apis_users', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='book_author_apis_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='book_author_apis_user',
    )

    class Meta(AbstractUser.Meta):
        db_table = 'user'


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    readers = models.ManyToManyField(User, related_name='books_read', blank=True)


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
