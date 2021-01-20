import tkinter #Documentation https://docs.python.org/3/library/tk.html
from random import randint
from tkinter import messagebox

low = 0
high = 20
rand = randint(low, high)

def check(guess):
    if guess < rand:
        tkinter.Label(tk, text=f"{guess} is too low").pack()
    elif guess > rand:
        tkinter.Label(tk, text=f"{guess} is too high").pack()
    else:
        tkinter.messagebox.showinfo(f"You WIN! {guess} is correct")

tk = tkinter.Tk()
tk.title("Programme")

label = tkinter.Label(tk, text=f"Guess a number {low} to {high} (inclusive)")
label.pack()

entry = tkinter.Entry()
entry.pack()

button = tkinter.Button(tk, text="Guess", command = lambda: check(int(entry.get())))
button.pack()

tk.mainloop()
print("Done")