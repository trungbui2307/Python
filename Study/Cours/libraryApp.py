from book import Book
import booksSDK

def print_menu():
    print("""Choose an option:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        for book in booksSDK.get_books():
            print(book)
    elif response == 2:
        print("What is the name of the book")
        name = input()
        print("How many pages is the book")
        pages = int(input())

        book = Book(name, pages)

        booksSDK.add_book(book)
    elif response == 3:
        print("What is the current title ")
        title = input()
        print("Current number of pages")
        pages = input()

        book = Book(title, pages)

        print("What is the current title")
        new_title = input()
        print("Current number of pages")
        new_pages = input()

        print(booksSDK.update_book(book, new_title, new_pages))


    elif response == 4:
        print("What is the title")
        title = input()
        print("Number of pages")
        pages = input()

        book = Book(title, pages)
        print(booksSDK.delete_book(book))

    