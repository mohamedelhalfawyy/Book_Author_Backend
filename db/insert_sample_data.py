import random
from django.contrib.auth.models import User
from Book_Author_APIS.models import Author, Book, Page


def insert_sample_data():
    # Create users
    users = []
    for i in range(5):
        if i < 2:
            # Create authors
            username = f"author{i + 1}"
            password = "password"  # Set the desired password
            email = f"author{i + 1}@example.com"
            user = User.objects.create_user(username=username, password=password, email=email)
            name = f"Author {i + 1}"
            author = Author.objects.create(user=user, name=name, email=email)
            users.append(author)
        else:
            # Create normal users
            username = f"user{i + 1}"
            password = "password"  # Set the desired password
            email = f"user{i + 1}@example.com"
            user = User.objects.create_user(username=username, password=password, email=email)
            users.append(user)

    # Create books
    books = []
    for user in users:
        if isinstance(user, Author):
            # For authors, create books
            title = f"Book by {user.name}"
            book = Book.objects.create(title=title, author=user)
            books.append(book)
        else:
            # For normal users, randomly select a book to read
            book = random.choice(books)
            book.readers.add(user)

    # Create page contents
    for book in books:
        for i in range(5):
            content = f"Content of Page {i + 1} for {book.title}"
            Page.objects.create(book=book, content=content)

    print("Sample data inserted successfully.")


# Call the function to insert sample data
insert_sample_data()
