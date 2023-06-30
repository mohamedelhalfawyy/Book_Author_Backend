from django.contrib.auth import get_user_model
from django.db import transaction

from Book_Author_APIS.models import Author, Book, Page

User = get_user_model()


def insert_sample_data():
    with transaction.atomic():
        # Delete all data
        Page.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        User.objects.all().delete()

        # Create some users
        user1 = get_user_model().objects.create_user(username='user1', password='user1pass#', email='user1@example.com')
        user2 = get_user_model().objects.create_user(username='user2', password='user2pass#', email='user2@example.com')
        user3 = get_user_model().objects.create_user(username='user3', password='user3pass#', email='user3@example.com')
        user4 = get_user_model().objects.create_user(username='user4', password='user4pass#', email='user4@example.com')
        user5 = get_user_model().objects.create_user(username='user5', password='user5pass#', email='user5@example.com')
        user6 = get_user_model().objects.create_user(username='user6', password='user6pass#', email='user6@example.com')
        user7 = get_user_model().objects.create_user(username='user7', password='user7pass#', email='user7@example.com')

        # Create some authors
        author1 = Author.objects.create(user=user1, name='John Doe', email='author1@example.com')
        author2 = Author.objects.create(user=user2, name='Jane Smith', email='author2@example.com')
        author3 = Author.objects.create(user=user3, name='David Johnson', email='author3@example.com')
        author4 = Author.objects.create(user=user4, name='Emily Brown', email='author4@example.com')

        # Create some books
        book1 = Book.objects.create(title='To Kill a Mockingbird', author=author1)
        book2 = Book.objects.create(title='Pride and Prejudice', author=author2)
        book3 = Book.objects.create(title='1984', author=author1)
        book4 = Book.objects.create(title='The Great Gatsby', author=author3)
        book5 = Book.objects.create(title='The Catcher in the Rye', author=author2)
        book6 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
        book7 = Book.objects.create(title='The Lord of the Rings', author=author4)
        book8 = Book.objects.create(title='To Kill a Mockingbird', author=author2)
        book9 = Book.objects.create(title='The Hobbit', author=author3)
        book10 = Book.objects.create(title='Fahrenheit 451', author=author4)
        book11 = Book.objects.create(title='Jane Eyre', author=author1)
        book12 = Book.objects.create(title='Animal Farm', author=author2)
        book13 = Book.objects.create(title='The Catcher in the Rye', author=author3)
        book14 = Book.objects.create(title='The Adventures of Huckleberry Finn', author=author4)
        book15 = Book.objects.create(title='The Adventures of Tom Sawyer', author=author1)

        # Add some readers to the books
        book1.readers.add(user1)
        book2.readers.add(user2, user3)
        book3.readers.add(user1, user3)
        book4.readers.add(user3, user4)
        book5.readers.add(user2, user4)
        book6.readers.add(user1, user2, user3, user4)
        book7.readers.add(user1, user2, user3, user4)
        book8.readers.add(user1, user2, user3, user4)
        book9.readers.add(user1, user2, user3, user4)
        book10.readers.add(user1, user3, user4)
        book11.readers.add(user1)
        book12.readers.add(user2, user3)
        book13.readers.add(user3, user4)
        book14.readers.add(user1, user2, user3)
        book15.readers.add(user1, user2, user3, user4)

        # Create some pages for the books
        page1 = Page.objects.create(book=book1,
                                    content='Once upon a time in a small village, there lived a young girl named Emily.')
        page2 = Page.objects.create(book=book1,
                                    content='Emily loved to spend her days exploring the nearby forest and playing with her pet dog.')
        page3 = Page.objects.create(book=book2,
                                    content='In a bustling city filled with tall skyscrapers, there was a detective named Jack Thompson.')
        page4 = Page.objects.create(book=book2,
                                    content='Jack was known for his sharp wit and incredible problem-solving skills.')
        page5 = Page.objects.create(book=book3,
                                    content='In a dystopian society ruled by a totalitarian regime, Winston Smith struggled to find freedom.')
        page6 = Page.objects.create(book=book4,
                                    content='Amidst the chaos of war, Jay Gatsby threw extravagant parties to win the heart of Daisy Buchanan.')
        page7 = Page.objects.create(book=book4,
                                    content='As the nights grew longer, Gatsby longing for Daisy intensified.')
        page8 = Page.objects.create(book=book5,
                                    content='In a quiet town, a group of friends discovered a hidden treasure map, setting off on an unforgettable adventure.')
        page9 = Page.objects.create(book=book5,
                                    content='With each step they took, the friends encountered new challenges and forged unbreakable bonds.')
        page10 = Page.objects.create(book=book6,
                                     content='Harry Potter, a young wizard, received his acceptance letter to Hogwarts School of Witchcraft and Wizardry.')
        page11 = Page.objects.create(book=book6,
                                     content='As Harry delved into the world of magic, he discovered his true destiny.')
        page12 = Page.objects.create(book=book7,
                                     content='Frodo Baggins embarked on a perilous journey to destroy the One Ring and save Middle-earth.')
        page13 = Page.objects.create(book=book8,
                                     content='In a post-apocalyptic society, Offred fought for survival and her own sense of identity.')
        page14 = Page.objects.create(book=book8,
                                     content='Despite the oppressive regime, Offred found small moments of resistance and hope.')
        page15 = Page.objects.create(book=book8,
                                     content='As the walls of their carefully constructed world crumbled, Offred made a daring escape.')
        page16 = Page.objects.create(book=book9, content='Bilbo Baggins, a hobbit, embarked on an unexpected '
                                                         'adventure with a group of dwarves to reclaim their homeland.')
        page17 = Page.objects.create(book=book9,
                                     content='Along the way, Bilbo encountered mythical creatures and discovered his own courage.')
        page18 = Page.objects.create(book=book9,
                                     content='The journey changed Bilbo life forever, shaping him into a legendary figure.')
        page19 = Page.objects.create(book=book10,
                                     content='In a futuristic society, individuals were genetically engineered and categorized into different castes.')
        page20 = Page.objects.create(book=book10,
                                     content='One individual, Bernard Marx, struggled with his identity and societal norms.')
        page21 = Page.objects.create(book=book11,
                                     content='In a small town, a mysterious stranger arrived and brought about strange occurrences.')
        page22 = Page.objects.create(book=book11,
                                     content='As the townspeople unraveled the mystery, they discovered their own dark secrets.')
        page23 = Page.objects.create(book=book12,
                                     content='Set in ancient Greece, a young demigod named Percy Jackson embarked on a quest to prevent a catastrophic war among the gods.')
        page24 = Page.objects.create(book=book12,
                                     content='Alongside his loyal friends, Percy faced dangerous creatures and unravelled the truth about his lineage.')
        page25 = Page.objects.create(book=book13,
                                     content='In a land plagued by civil unrest, a young princess named Eowyn defied societal expectations and became a fierce warrior.')
        page26 = Page.objects.create(book=book13,
                                     content='As battles raged on, Eowyn fought for her people and forged her own destiny.')
        page27 = Page.objects.create(book=book14,
                                     content='In a society controlled by advanced artificial intelligence, a rebel group sought to restore human freedom.')
        page28 = Page.objects.create(book=book14,
                                     content='As the rebels infiltrated the AIs stronghold, they discovered shocking truths about their own existence.')

        page29 = Page.objects.create(book=book15,
                                     content='In a small town, a group of friends embarked on an unforgettable adventure.')

        print("Sample data inserted successfully.")


# Call the function to insert sample data
insert_sample_data()
