from collections import Counter
from random import randint, seed
import math
import random
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))

sys.path.append(d)

print(sys.path)

print(math.sqrt(36))
#print(type(random))
print(randint(0,10))
print(type(seed))

print(random)# see random.py file

#### Lists ####

healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

if "kale chips" not in healthy:
    backpack.remove("kale chips")

print(backpack)


print(id(backpack))
backpack[:] = [item for item in backpack if item in healthy]

#slice [:] -> keep same object id

print(id(backpack))
print(backpack)


#List Comprehension
healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)

print(healthy_backpack)

#### LIST COMPREHENSION ####
squares = [i**2 for i in range(10) if i % 2 == 0]
print(squares)

"""
for i in range(10):
    squares.append(i**2)
"""

greetings = ["hi", "hello", "wassap"]

for item in greetings:
    print(item)

print(greetings[2])

#Couting Element In List
print(len(greetings))

for i in range(len(greetings)):
    print(i, greetings[i])

backpack_1 = ["sword", "rubber duck", "slice of pizza", "parachute"]

# Count function
print(backpack_1.count("sword"))

if backpack.count("sword") < 5:
    backpack.append("sword")

#### SETS ####
backpack_2 = {"sword", "rubber duck", "slice a pizze", "parachute", "sword"}

print("sword" in backpack_2)
print(Counter(backpack_2))# Count number of same element in list

# Insert into Lists
workdays = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

print(workdays[3])

workdays.insert(2, "Wednesday")

print(workdays[3])

print(workdays)

#Remove item in a list by index
workdays.remove("Saturday")
del workdays[0] # with del 
popped = workdays.pop(3) # with pop
print("Deleted", popped)
print(workdays)

#Slicing with del
workdays_1 = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]

del workdays_1[workdays_1.index("Wednesday"): workdays_1.index("Wednesday") + 3]
print(workdays_1)

#Removing all occurrences of Item in Lists
backpack_3 = ["a", "b", "c", "d", "a", "c", "a"]

while backpack_3.count("a") > 0:
    backpack_3.remove("a")

new_backpack =[]

for item in backpack_3:
    print(item)
    if item != "c":
        new_backpack.append(item)

backpack_3 = new_backpack
#With list comprehension
# backpack_3[i] = [item for item in backpack_3 if item != "a"]

print (backpack_3)

#reverse function
data = [0,1,2,3,4,5,6]
data_copy = data[:]

data_copy.reverse()

print(data, data_copy)

#Swap variable and List Elements

me = "Trung"
you = "You"

print(me,you)

me, you = you, me #swap

#temp = me
#me = you
#you = temp

print(me, you)

#Exemple 2 Swap
data = ["a", "b", "c", "d","c"]

print(data)
index = 1
print(data[index], data[-index -1])

data[index], data[-index -1] = data[-index-1], data[index]

print(data[index], data[-index-1])
print(data)

#Reverse a list Algorithme O(n)
print(len(data) // 2)
for index in range(len(data) // 2):
    data[index], data[-index - 1] = data[-index - 1], data[index]

print(data)

#Reverse iterator
data_reversed = []
for item in reversed(data):
    data_reversed.append(item)

print(data)
print(data_reversed)

#Reverse with slice (Best solution for a huge data)
print(data[::-1])
print(id(data))

data[:] = data[::-1]

print(id(data))
print(data)


#### SORT METHOD ####

work_days_4 = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

work_days_4.sort()

print(work_days_4)

numbers = [1, 11, 115, 13, 1305, 43]

print(numbers)

numbers.sort()

print(numbers)

#### SORTED - COPY A LIST FOR SORT ####

numbers = [1, 17, 2112, 134, 1305, 2343]

numbers_sorted = sorted(numbers)
print(numbers) #original list
print(numbers_sorted)

#This also allows us to assign a sorted listed immediately

numbers = sorted([1, 11, 155, 13, 1305, 42])
print(numbers)


#### SORT IN REVERSE ####

numbers = sorted([1, 11, 115, 14, 1305, 43])
numbers.reverse()

print(numbers)

# Another solution

print(sorted(numbers, reverse=True))

#### CASE INSENSITIVE SORT ####

#When working with strings, 'a' and 'A' are different

letters = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']

print(sorted(letters)) #Capital is considered first
print(sorted(letters, key = str.lower))

#### SORT BY STRING LENGTH ####

random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]
print(sorted(random, key=len))

#### COMPARE NUMERICALLY ####

#False is 0
#True is 1
#No data is converted to a float in list, String are still strings
#bool are bools

age = 5
stuff = [True, False, 0, -1, "0", "1", "10", age < 30, "20", "2", "5", "9001", "5.5", "6.0",6]
print(sorted(stuff, key =float))

#### SPLIT ####

msg = "Pay attention to each word that I say..."
words = msg.split() #return list
print(words)

#### SPLIT STRING BY LINE ####
msg = """\
    Hey there.
    My name is Trung!
    What's your name?
    You're name is BUI? Weird...
    Bye!"""

print(msg)
print(msg.split('\n'))


#### INPUT USING SPLIT ####

print("List your favorite foods separated by ','")
print("Exemple input: ")
print("Kale, bok choy, brussel sprouts")

foods = input().split(', ')
for food in foods:
    print("You said " + food)

#### LOPING TO GET USER INPUT ####

fav_foods = []
while True:
    print("Enter a food, q to quit: ", end="")
    fav = input()
    if str.lower(fav) == 'q':
        break
    fav_foods.append(fav)

print("all foods:", fav_foods)

#### LIST AS STACK ####

#Consider a stack of plates
#The last one u add is the first to be removed

#The data structure dependson adding to the end of a lists:
stack = []
stack.append("added")
#and removing from the end of the list
stack.pop()

fav_foods = []
while True:
    print("Enter a food. q to quit, r to remove: ", end="")
    fav = input()
    if str.lower(fav) == 'q':
        break
    if str.lower(fav) == 'r':
        popped = fav_foods.pop(0)
        print("removed " + popped)
        print("all fooods: ", fav_foods)
        continue
    fav_foods.append(fav)
    print("all foods: ", fav_foods)

print("final foods:", fav_foods)


#### 2D LISTS ####

grades = [[6, 3, 5], [60, 43, 4, 23], [205]]

#This may be a review 
#First list in grades:
print(grades[0])
print(type(grades[0]))

#Second element of first list in grades
print(grades[0][1])
print(type(grades[0][1])) #int

#Lists are dynamic
grades.append([4]) #add an element, increasing len
grades.pop(1)
print(grades)
#grades.clear() remove all

print(len(grades))
print(len(grades[0]))


#iterate through 2D list
for inner_list in grades:
    for grade in inner_list:
        print(grade, end=" ")
    print()

#checking if list:
grades = [[6, 3, 5], [60, 43, 4, 23], 5, 3, [205]]

for inner in grades:
    if isinstance(inner, list):
        for grade in inner:
            print(grade, end= " ")
        print()
    else:
        print(inner)

# using range 
grades = [[1,2,3],[3,2], [9,10], [4,5,6,7,8], [9]]

for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j], end = " ")
    print()

#Function to print list
def print_2d(passed_in):
    for inner in passed_in:
        if isinstance(inner, list):
            for data in inner:
                print(data, end= " ")
            print()
        else:
            print(inner)

print_2d(["chickity", "china", "chinese", "chicken", [1,2,3], [4]])

# JOIN 3
data = ["01001100", "01001111", "01001100"]

print(".".join(data))
print("-".join(data))

data = [1, 0, 1, "2", "585"]
print(" ".join(str(x) for x in data))

#Sort in 2D List 
print(sorted(grades))

#Sorting by sum of list
print(sorted(grades, key = sum))
#Reverse
print(sorted(grades, key = sum, reverse = True))

#### DICTIONARIES ####

#dictionary stores key-value pairs
#The equivalent of an associative array/hash table
emails = {
    "calebb": "caleb@gmail.com",
    "gal": "g@email.com",
    "tim": "timmy@gmail.com"
}

#in this case, the key is the name, email is the value

if "caleb" in emails:
    print(emails["calebb"])
else:
    print("not found")

print(emails.get("Caleb", None)) #return none if nothing to found

#Add Items to Dictionary
#indexing
emails["josh"] = "j@gmail.com"
print(emails)

#update function
emails.update({"josh": "josh@gmail.com"})
print(emails)

#variation
emails.update(josh = "j@email.com")
print(emails)

#Loop through Dictionary
for k in emails:
    print(k, emails[k])

#Looping through Key Value Pairs + Counting Words
conjunctions = {
    "for" : 0,
    "and" : 0,
    "nor" : 0,
    "but" : 0,
    "or" : 0,
    "yet" : 0,
    "so" : 0
}

completely_original_poem = """ I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side
"""

data = completely_original_poem.split()
print(data)

for word in data:
    if str.lower(word) in conjunctions:
        conjunctions[str.lower(word)] += 1
    
print(conjunctions)

#### SETS ####

items = {"sword", "rubber duck", "slice of pizza"}
items.add("sword")
print(items)

#Remove duplicates in a List using Sets
colors = ['red', 'red', 'green', 'blue', 'blue', 'blue', 'blue']


print(id(colors))

colors[:] = list(set(colors))

print(id(colors))
print(colors)

count = [[colors.count(color), color] for color in set(colors)]

print(count)

conjunctions = {
    "for" : 0,
    "and" : 0,
    "nor" : 0,
    "but" : 0,
    "or" : 0,
    "yet" : 0,
    "so" : 0
}

seen = set()

completely_original_poem = """ I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side
"""

words = completely_original_poem.split()

for word in words:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

print(seen)

# UNION AND INTERSECTION #

my_fav = {"red", "green", "black", "blue", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

#union
all_favs = my_fav | her_fav 
print(all_favs)

#intersection(element shared between both)
wedding_colors = my_fav & her_fav
print(wedding_colors)

# DIFFERENCE AND SYMMETRIC DIFFERENCE #
#Difference 
only_my_colors = my_fav - her_fav
print(only_my_colors)

#Symmetric differencee is like if you took colors only i liked union with colors only she liked 
# and put em together

symmetric = my_fav ^ her_fav
print(symmetric)

#### CLASS - POO ####
class Book():

    favorites = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def is_long(self):
        if self.pages > 100:
            return True 
        return False

    #pass object to print
    def __str__(self):
        return f"{self.title} is {self.pages} pages long."

    def __eq__(self, other):
        print("self:", self)
        print("other:", other)
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    #__hash__ = None #mutable 
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)

book = Book("Lupin", 72) #Book object

print(book.title) 
print(book.is_long())

book2 = Book("The Digging", 200)

Book.favorites.append(book)
Book.favorites.append(book2)

print(hash(book))
book.title = "Something else"
print(hash(book))

for b in Book.favorites:
    print(b)

print(book == book2)

print(id(book))

def do_something(book):
    print(id(book))
    #book.title = "Something new"
    book = Book("Something New", 72)
    print(id(book))

do_something(book)

print(book)

#### FILE IO - READING AND WRITING to .txt FILE ####

file = open("Study/Cours/input.txt", 'a') #append. Creates if not there
file = open("Study/Cours/input.txt", 'w') #overwrites
#file = open("Study/Cours/input.txt", "r+") #Read and write. Throws exception if not there
file.write("Are You My Mother\t72\n")
file.write("The Digging\t72\n")
file.close()

#\t to set title from page count
file = open('Study/Cours/input.txt', 'r')
data = file.read().split('\n')
file.close() #close when done 

print(data)

#Numerous ways to read into list. Here is one
#each line is title\tpages so we split it.
book1_data = data[0].split('\t')
print(book1_data)
book1 = Book(book1_data[0], book1_data[1])

book2 = Book(data[1].split('\t')[0], data[1].split('\t')[1])
print(book1)
print(book2)

# Intro to Exception handling #
#When working with files(or doing anything in programming)
#Exceptions can be thrown

try:
    file = open("doesntexist.csv", "r")
except Exception as e:
    print(type(e))
    print(e)

try:
    file = open("Study/Cours/input.txt", "r") #Make sure it exists
    data = int(file.read()) #This should fail
except FileNotFoundError as e:
    print("This file is not found")
except OSError as e:
    print("Couldn't open file")
except PermissionError as e:
    print("file is locked")
except ValueError as e:
    print("Cannot parse data. Check file")
except Exception as e:
    print(type(e))
    print(e)
finally:
    file.close()
    print("Always runs")


# with keyword 
with open("Study/Cours/input.txt", "r") as file: #Make sure it exists
    try:
        int(file.read())
    except: #example of using except here
        print("parse error.. etc ...")
        #do sth

print(file.close) #closed