import sqlite3

conn = sqlite3.connect("Study/Cours/database.db")

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books 
            (title TEXT, pages INTEGER)''')

#c.execute('INSERT INTO books (title) VALUES ("Lupin")')
#conn.commit()

books = [
    ("Are You My Mother?", 72),
    ("The digging-est Dog", 72),
    ("The Giving Tree", 66)
]

c.executemany('INSERT INTO books VALUES(?,?)', books)
conn.commit()

c.execute('SELECT * FROM books WHERE title = "Are You My Mother?"')
data = c.fetchall()
print(data)

c.execute('DELETE FROM books WHERE title="Lupin"')
conn.commit()

c.execute('UPDATE books SET title="New Book" WHERE rowid = 2')
conn.commit()

#update_book(book, "New Title")

c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)

### CREATE AN SDK ###

import booksSDK
from book import Book

book = Book("Are You My Mother?", 1000)
print("Added book id:", booksSDK.add_book(book))
print("Get book by title:", booksSDK.get_book_by_title(book.title))
print("Not a valid book:", booksSDK.get_book_by_title("yeet"))

booksSDK.add_book(Book('The Digging-est Dog', 76))
print("get books:", booksSDK.get_books())

book = booksSDK.update_book(book, book.title, 76)
print("Updated book:", book)
print("Deleted:", booksSDK.delete_book(book))
print("After delete:", booksSDK.get_book_by_title("Are You My Mother?"))

print("All books:", booksSDK.get_books())