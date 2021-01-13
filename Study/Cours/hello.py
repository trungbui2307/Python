print(5 + 5, "hey", 10.3,  "hi", end = "") 

age = 5
print(age)

import math
import copy

#OPERATOR
result = 10 // 3 # floor version = 3 
result2 = 10 / 3 # 3.33333
print(result2)
#new_result =  math.floor(result) #integer division 
print(math.ceil(result)) #math.ceil làm tròn lên 
print(result)
val = 10/5 + 3 * 3
print(val)

#Modulus
print(78 % 11)

#Raising Numbers to a Power
print(3 ** 3)
result = math.pow(3,5)
new_version = math.floor(result)
print(new_version)

#STRING
msg = "Hello World"
print(msg)
msg1 = "Hello\nHey" # \n newline
print(msg1)
msg2 = "\x41" # ASCII value 
print(msg2)

msg3 = "you're so cute"
msg4 = "hmu"
full_message = msg3 + "..." + msg4 #Concatenation
print(full_message)
print(full_message + "...there") #Concatenation automatic

#skip newline using 
print("""\
Name: Trung.\
Age: 58""")

#INDEXES
poem = "Where am I?"
print(poem[0] + poem[6])
print(poem[:4]) #Slicing Strings
print(poem[4:]) 
print(poem[-5:]) #negative 
print(poem[6:8]) #with two numbers
start_of_last = 6
print(poem[start_of_last:start_of_last+4])

#len() Function

msg = "please subscribe"
print(len(msg))
print(msg[15])

#Convert int to String
print("Your message was " + str(len(msg)) + " characters long")

#Function Calls
age = 15
age_str = str(age)
print(str(age))
id_age_str = id(age_str)
print(id(age_str))
other = math.floor(2.6)
print(math.floor(2.6))
added = id_age_str + other 
print(added)
print(str(added))
added_str = str(added)
length = len(added_str)
print(length)

print(len(str(id(str(age)) + math.floor(2.6))))

#List and Indexing
ages= [12, 18, 28]
people = ["Caleb", "Sabrina", "Emily"]

#We can mix types of data
#Nested List
my_favorite_things = ["Working out", 7, ['amazon prime',[ 'netflix', 'huhu']]]
c = copy.deepcopy(my_favorite_things)


print(ages)
print(people)
print(my_favorite_things)

print(id(my_favorite_things))

my_favorite_things[0] = "Walking"

print(my_favorite_things)
print(len(my_favorite_things))
print(my_favorite_things[1:2])

copy = my_favorite_things.copy()
print(my_favorite_things,copy)

copy[0] = "------"

print(my_favorite_things, copy)

print(my_favorite_things[2][1])

print(my_favorite_things[2][1][0])

copy[2][0] = "HELO"

print(id(copy[2]))
print(id(my_favorite_things[2]))

print(my_favorite_things, copy)

print(my_favorite_things, c)

### Combining Lists(Concatenation) ###

least_favorite_things = ["onions", "java"]
print(my_favorite_things + least_favorite_things)

least_favorite_things.append("editing")
print(least_favorite_things)

#INPUT

print("Hey What's your name")
name = input()
print("Hello, " + name)

#IF STATEMENT
print("What's your age?")
age = int(input()) 

if age > 20:
    print("Welcome")
elif age <= 15:
    print("Bai bai")
else:
    print("Oh!")

print("Merci")

subscribed = True
points = 50

if subscribed or points: #OR Operator
    points = 60
print ("....")

if subscribed and points: #AND Operator
    point = 25

if not subscribed:
    print("....")

# Compare strings
me = "Trung"
you = "Nerd"
print("me == you?", me == you)

#Even lists!
my_grades = [100, 100, 100]
your_grades = [100, 100, 1]
print("Same grades?", my_grades == your_grades) #false
print("Same grades?", my_grades is your_grades)

#For loop

friends = ["Abby", "Jonathan", "Becky", "Ryan"]

for friend in friends:
    #print(friend)
    print(friend, end = " ")
print()

#range() function for loop

sum = 0


for i in range(10):
    print(i)
    sum += 1

print(sum)

for i in range(10, 20):
    print(i,end= " ")
print()

for i in range(200, 0, -1):
    print(i, end=" ")
print()

#Nested Loop
print("Nested Loop")
for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print()

print("Nested Loop with range")
for i in range(4):
    for j in range(i):
        print(j, end=" ")
    print()

#Create a list from loop
my_list = list(range(10))
print(my_list)

#Loop with index
foods = ["asparagus", "tacos", "strawberries", "yogurt", "bagels"]

for i in range(len(foods)):
    print(i,foods[i], end = " ")
print()

languages = ["C++", "Java", "Python", "Javascript"]

print("What are u searching for?")
lang = input()

for language in languages:
    print(language)
    if(language == lang):
        print("We found " + lang)
        break #with break
    print("end of loop")

for language in languages:
    print(language)
    if(language == lang):
        print("We found " + lang)
        continue #with continue
    print(language + "... Not what we're looking for...")


for language in languages:
    print(language)
    if(language == lang):
        pass #key-word to pass the statement

#While loop
i = 0
while i < 10:
    print(i)
    i += 2


numbers = [4,3,6,19,23,54,2,5]

i = 0
square = 500
succes = False
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "squared is larger than", square)
        succes = True
        break
    print(numbers[i], "squared is not larger than", square)
    i += 1
else:
    print("None square are larger than 500")
if not succes:
    print("None were large enough!")

print ("Do u want to continue? Y/N")
response = input()
while response == "Y":
    print("Do you want to continue? Y/N")
    response = input()
    if response.lower() != 'y': # lower case function
        break

while True:
    print("Q to quit. Continuing ...")
    response = input()
    if response == "Q":
        break

#Nested If
logging = False
logging_in = True 
name = "TRUNG"

if logging_in:
    if logging:
        print(name + " is logging in")
    print("Welcome, " + name)

############ FUNCTION ############

#Create a Function:
def greet():
    print("Hey there")
    print("Welcome, Trung!")

greet()

#with parameter
def greet1(name):
    print("Hey there")
    print("Welcome, " + name)

greet1("Trung")

#with return 
def greet2(name):
    if name == "Trung":
        print("Blah blah")
        return 
    return "Bleh Bleh"
    print("Hey, Hello")

print(greet2("Trun"))

#default Parameter
def greet3(name= "User"):
    if name == "Trung":
        print("Blah blah")
        return 
    return "Bleh Bleh"
    print("Hey, Hello")

print(greet3())

#with multiple Arguments
def greet4(name= "User", be_nice = True):
    if not be_nice:
        print("Blah blah")
        return 
    return "Bleh Bleh"
    print("Hey, Hello")

print(greet4())
print(greet4(be_nice=False))
print(greet4("Trung", False))

# In function, / in parameter is that everything on the left is by position only
# and * is that on the right is by name only

#Function to Work with Lists
def greet_all(people):
    for person in people:
        print("Hello " + person)

friends = ["Bob", "Josh", "Austin"]

greet_all(people)

#Function taking unlimited Arguments
def greet2(person, first_time = False):
    if first_time:
        return "First time for everything, right? Welcome, " + person
    return "Hello, " + person

def greet_all1(people):
    for person in people:
        print(greet2(person, True))

greet_all1(friends)

#Unpacking Data
def print_info(name, age, email):
    print(name + " is " + str(age) + ". Reached at " + email)

info = ["Trung",12, "trungbuias@gmail.com"]

print_info(info[0], info[1], info[2])
print_info(*info)