import tkinter 
from tkinter import END
from book import Book
import booksSDK

books = []

def add_to_list():
    book = Book(title_entry.get(), pages_entry.get())

    if(booksSDK.add_book(book)):
        books.append(book)
        listbox.insert(END,book)
        title_entry.delete(0, END)
        pages_entry.delete(0, END)

    
def remove_from_list():
    book_tuple = listbox.curselection()
    book = books.pop(book_tuple[0])
    if(booksSDK.delete_book(book)):
        listbox.delete(book_tuple)

tk = tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.pack()

for book in booksSDK.get_books():
    books.append(book)
    listbox.insert(END, book)

title_entry = tkinter.Label(tk, text="Book Title:")
title_entry.pack()

#listbox.insert(0, "hello", "hi", "yo")
#listbox.insert(END, "hello", "hi", "yo")
#listbox.insert(END, "hoho")
#listbox.delete(0)

title_entry = tkinter.Entry(tk)
title_entry.pack()

pages_entry= tkinter.Label(tk, text="Book Pages:")
pages_entry.pack()

pages_entry = tkinter.Entry(tk)
pages_entry.pack()

button = tkinter.Button(tk, text = "Add Value", command=add_to_list)
button.pack()

button = tkinter.Button(tk, text = "Remove Selected Book", command=remove_from_list)
button.pack()


tk.mainloop()