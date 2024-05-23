class Book:
    def __init__(self, title, author, isbn, genre, pub_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.pub_date = pub_date
        self.books = []

class add_book(Book):
        
    def __init__(self, title, author, isbn, genre, pub_date):
        super().__init__(title, author, isbn, genre, pub_date)

        self.books.append({title:{'author':author, 'ISBN':isbn, 'genre': genre, 'publication date': pub_date, 'availability': availability}})
        print(self.books)

title = input('Please enter the title of the book: ')
author = input('Please enter the author of the book: ')
isbn = input('Please enter the ISBN of the book: ')
genre = input('Please enter the genre of the book: ')
pub_date = input('Please enter the publication date of the book: ')
availability = True

add_book()