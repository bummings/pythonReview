
# Save yrself some trouble and set an alias for python and python3:
# like dis:   alias python=python3

numOfCats = 99;

# a dict (dictionary) is like an object in javascript
myDict = {"first_name": "faux", "last_name": "graf", "age": 33, "bruhs": ["larry", "mo", "ricky"]}

# None is the Python's equivalent of 'null' in other programming languages, represents nothingness
lonesomeBruh = {'first name': 'loro', 'last_name': 'ipso', 'age': 24, 'bruhs': None}

# concatenation, yo
name1 = 'edison'
name2 = 'allen';
nameFull = name1 + " " + name2

# f-strings for interpolation
number = 99
print(f"I've told ya {number} times now, bruh.")

print(nameFull)
print(myDict)
print(lonesomeBruh);
print('say \nbruhhhh')


# converting data types: self-explanitory, no?
decimal = 420.6969
integer = int(decimal)
print(f"This is a converted data type, you unwavering polyglot: {integer}")

# the almighty LIST: aka arrays in Python
my_list = [1, 2, 3]
my_list_as_string = str(my_list)
print(f"This is the original list, homeboy: {my_list}")
print(f"This is a converted list into an array, aye: {my_list_as_string}")

# inside yr python terminal: converting types, etc
# 
# >>> num = 420
# >>> type(num)       // int
# >>> num = float(num)
# >>> num            // 420.0
# >>> type(num)      // float

# conditionals, my man

print("\n")
print("What's the name my man")
name = input()
name = name.lower()

# Python is real into indentation and semicolons- no curly brackets here :[
if name == 'faux':
  print('sup faux')
elif name == 'graf':
  print('graf in the house')
else:
  print("who the hell are you?")


# 2-8: 2 dollar ticket
# 65+: 5 dollar ticket
# everyone else: 10 dollar ticket
age = 2

if (age >= 2 and age <= 8):
  print('child price')
elif (age >= 65):
  print('senior citizen price')
else:
  print('normal price')
 
