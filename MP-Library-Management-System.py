#Task 1

class Library:
    def __init__(self):
        self.books = []
        self.authors = []
        self.genres = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.check_out():
            print(f"Book '{title}' has beeen lent out\n")
        else:
            print(f"Book '{title}' is not available\n")
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned\n")
        else:
            print(f"Book '{title}' not found in library\n")

    def display_books(self):
        print("Library Catalogue:")
        for book in self.books:
            print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}\nGenre: {book.genre}\nPublication Date: {book.pub_date}\n")

    def add_user(self, user):
        self.users.append(user)

    def view_user(self, lib_id):
        for user in self.users:
            if user.lib_id == lib_id:
                return user
        return None
    
    def display_users(self):
        print('Library Users:')
        for user in self.users:
            print(f'User: {user.name}\nLibrary ID: {user.lib_id}\n')
    
    def add_author(self,author):
        self.authors.append(author)

    def view_author(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None
    
    def display_authors(self):
        print('\nAuthors: ')
        for author in self.authors:
            print(f'Name: {author.name}\nBio: {author.bio}\n')

    def add_genre(self, genre):
        self.genres.append(genre)

    def view_genre(self,genre):
        for genre in self.genres:
            if genre.name == name:
                return genre
        return None
    
    def display_genres(self):
        print('Genres: ')
        for genre in self.genres:
            print(f'Genre: {genre.name}\nCategory: {genre.category}\nDescription: {genre.description}\n')
        



class Book:
    def __init__(self, title, author, isbn, genre, pub_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.pub_date = pub_date
        self.is_available = True
    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True

class User:
    def __init__(self, name, lib_id):
        self.name = name
        self.lib_id = lib_id

class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

library = Library()

while True:
    print('\nLibrary Management System')
    print('1. Book Operations')
    print('2. User Operations')
    print('3. Author Operations')
    print('4. Genre Operations')
    print('5. Exit')
    choice = input('\nSelect one of the above choices: ')

    if choice == '1':
        print('Book Operations')
        print('1. Add a new book')
        print('2. Borrow a book')
        print('3. Return a book')
        print('4. Search for a book')
        print('5. Display all books')
        book_choice = input('\nSelect one of the above choices: ')

        if book_choice == '1':
            title = input('Please enter the title of the book: ')
            author = input('Please enter the author of the book: ')
            isbn = input('Please enter the ISBN of the book: ')
            genre = input('Please enter the genre of the book: ')
            pub_date = input('Please enter the publication date of the book: ')
            availability = True
            library.add_book(Book(title, author, isbn, genre, pub_date))

        elif book_choice == '2':
            title = input("Enter the title of the book you'd like to check out: ")
            library.lend_book(title)

        elif book_choice == '3':
            title = input('Enter book title to return: ')
            library.return_book(title)

        elif book_choice == '4':
            title = input('Enter book title to search: ')
            book = library.find_book(title)
            if book:
                availability = 'available' if book.is_available else 'not available'
                print(f"'{title}' by {book.author} is {availability}")
            else:
                print(f"Book '{title}' not found")

        elif book_choice == '5':
            library.display_books()
        else:
            print('Invalid option please try again')


    elif choice == '2':
        print('User Operations')
        print('1. Add a new user')
        print('2. View user details')
        print('3. Display all users')
        user_choice = input('\nSelect one of the above choices: ')
        if user_choice == '1':
            name = input('Please enter the name of the user to add: ')
            lib_id = input('Please enter the new users libray ID: ')
            library.add_user(User(name, lib_id))

        elif user_choice == '2':
            id_input = input('Please enter the library ID of the user to view: ')
            user = library.view_user(id_input)
            if user:
                print(f'Name: {user.name}\nLibrary ID: {user.lib_id}')
            else:
                print(f"User '{user}' not found")

        elif user_choice == '3':
            library.display_users()

        else:
            print('Invalid option please try again')

        
    elif choice == '3':
        print('Author Operations')
        print('1. Add a new author')
        print('2. View author details')
        print('3. Display all authors')
        author_choice = input('\nSelect one of the above choices: ')
        if author_choice == '1':
            name = input('Please enter the name of the author to add: ')
            bio = input('Please enter a short bio for the author: ')
            library.add_author(Author(name, bio))
        elif author_choice == '2':
            name_input = input('Please enter the name of the author to view: ')
            author = library.view_author(name)
            if author:
                print(f'Name: {author.name}\nBio: {author.bio}\n')
        elif author_choice == '3':
            library.display_authors()
        else:
            print('Invalid option please try again')


    elif choice == '4':
        print('Genre Operations')
        print('1. Add a new genre')
        print('2. View genre details')
        print('3. Display all genres')
        genre_choice = input('\nSelect one of the above choices: ')
        if genre_choice == '1':
            name = input("Please enter the name of the genre to add: ")
            description = input("Please enter a description of the genre to add: ")
            category = input("Please enter the category of the genre to add: ")
            library.add_genre(Genre(name, description, category))

        elif genre_choice == '2':
            genre_input = input('Please enter the name of the genre to view: ')
            genre = library.view_genre(name)
            if genre:
                print(f'Genre: {genre.name}\nCategory: {genre.category}\nDescription: {genre.description}\n')
        elif genre_choice == '3':
            library.display_genres()
        else:
            print('Invalid option please try again')

    elif choice == '5':
        print('\nClosing Library Management System')
        break
    else:
        print('Invalid option please try again')