from collections import Counter

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
print(numbers)
print(numbers_sorted)

#This also allows us to assign a sorted listed immediately

numbers = sorted([1, 11, 155, 13, 1305, 42])
print(numbers)

