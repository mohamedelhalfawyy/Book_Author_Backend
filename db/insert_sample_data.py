from Book_Author_APIS.models import Author, Book, Page, User
from django.db import transaction


def insert_sample_data():
    with transaction.atomic():
        # Delete all data
        Page.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        User.objects.all().delete()

        # Create some users
        user1 = User.objects.create_user(username='user1', password='user1pass', first_name='User', last_name='One', email='user1@example.com')
        user2 = User.objects.create_user(username='user2', password='user2pass', first_name='User', last_name='Two', email='user2@example.com')
        user3 = User.objects.create_user(username='user3', password='user3pass', first_name='User', last_name='Three', email='user3@example.com')
        user4 = User.objects.create_user(username='user4', password='user4pass', first_name='User', last_name='Four', email='user4@example.com')

        # Create some authors
        author1 = Author.objects.create(user=user1, name='Author One', email='author1@example.com')
        author2 = Author.objects.create(user=user2, name='Author Two', email='author2@example.com')
        author3 = Author.objects.create(user=user3, name='Author Three', email='author3@example.com')

        # Create some books
        book1 = Book.objects.create(title='Book One', author=author1)
        book2 = Book.objects.create(title='Book Two', author=author2)
        book3 = Book.objects.create(title='Book Three', author=author1)
        book4 = Book.objects.create(title='Book Four', author=author3)
        book5 = Book.objects.create(title='Book Five', author=author2)

        # Add some readers to the books
        book1.readers.add(user1, user2)
        book2.readers.add(user2, user3)
        book3.readers.add(user1, user3)
        book4.readers.add(user3, user4)
        book5.readers.add(user2, user4)

        # Create some pages for the books
        page1 = Page.objects.create(book=book1, content='This is the first page of book one.')
        page2 = Page.objects.create(book=book1, content='This is the second page of book one.')
        page3 = Page.objects.create(book=book2, content='This is the first page of book two.')
        page4 = Page.objects.create(book=book3, content='This is the first page of book three.')
        page5 = Page.objects.create(book=book4, content='This is the first page of book four.')
        page6 = Page.objects.create(book=book4, content='This is the second page of book four.')
        page7 = Page.objects.create(book=book5, content='This is the first page of book five.')

        print("Sample data inserted successfully.")


# Call the function to insert sample data
insert_sample_data()
