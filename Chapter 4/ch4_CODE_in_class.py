"""
    - Tuples
    - Functions
    - Dictionaries
    - File Operations
    - OS Module (if time)
"""
from PIL.Image import register_extension

# --- Slide 3 Tuples
# cards = ()  # Empty tuple container
# print(type(cards))

# cards = (6,7, 'Ace')
# cards_full = ((2, 'hearts'), (3, 'spades'))
#
# cars = ([2016, 'Ford', 'Fusion'], [2023, 'Toyota', 'Prius'])


# Get element info from a tuple (similar to lists and string)
# print(cards_full[1])
# print(cards_full[1][1])


# --- Demonstrates you can't modify a tuple like you can a list
# cards[2] = 'King' # Can't change a tuple element
# print(cars[0])
# cars[0][2] = 'Model T'
# print(cars)

# cars[0] = ('Landrovee') # Can't change this


# cards = list(cards) # If we change the cards tuple to a list we can manipulate elements
# print(cards)
# cards.append('King')
# print(cards)

# cards = tuple(cards)
# print(cards)
#
# print(hash(cards))


# --- Slide 4 Tuple Quick task
"""
Create a tuple named student containing:

    - Your first name (String)
    - Number of hours of sleep you got last night (Float)
    - Your current caffeine level from 0–10  (Int)
    - Your favorite food  (String) 

Then:
    - Print your entire student profile. 
    - Use an index to print your caffeine level. 
    - Use an index to print your favorite food. 
    - Try to change your hours of sleep to 10. 
    - Explain: What happens? Why?
"""
pass




# --- Slide 6 Tuple Application - Building a Card deck for a game
import random

# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace')

# deck = []
# for suit in suit_tuple:
#     for rank in rank_tuple:
#         card = (rank, suit) # Temporary variable to store the current card in loop
#         # print(card) # Show the card for debugging
#         deck.append(card)  # Add this card to the deck list

# print(deck)
# print(len(deck))
#
# random.shuffle(deck)
# print(deck)
#
# print(random.choice(deck))
# print(random.choices(deck, k=5))


# --- Slide 8 Defining Functions
# def greeting():
#     print('Hi Everyone')

# greeting() # Call The function
# greeting()

# greeting  # Calling greeting without parenthesis (), does NOT run the function
# print(greeting)  # printing greeting without parenthesis, shows where the function is stored in computer memory
# print(greeting())  # Prints None because our function (greeting) does not return anything



# --- Slide 9 The return statement
# def greeting():
#     print('Hi everyone')
#     return 'more stuff'
    # print('goodbye') # return kills the function

# greeting()  # Does not display anything

# message = greeting()  # Call the function and save what it returns to a variable
# print(message)


# ANOTHER EXAMPLE
# def add():
#     a = 2
#     b = 3
#     return a + b # return 5 back to the main program
#
# answer = add()
# print(answer)
# print(answer ** 2) # prints 25

# print(add())






# --- Slide 10 Defining Functions with POSITIONAL PARAMETERS
# def greeting(first_name, last_name):
#     print(first_name)
#     return f"Hi {first_name} {last_name}, what's up?"
#
# my_greeting = greeting(3.1415926, 'Drubinskiy')
# print(my_greeting)


# --- Slide 11 Defining Functions with KEYWORD PARAMETERS
# def greeting(first_name = 'Jon', last_name = 'Doe'):
#     return f"Call me {last_name}, {first_name}, {last_name}"
#
# my_greeting = greeting()
# print(my_greeting)
#
# my_greeting = greeting(first_name='James')
# print(my_greeting)
#
# my_greeting = greeting(last_name='Bond', first_name='James')
# print(my_greeting)
#
# my_greeting = greeting(first_name='James', last_name='Bond')
# print(my_greeting)
#
# # my_greeting = greeting(first_name='James', 'Bond')
# my_greeting = greeting('James', last_name='Bond')
# print(my_greeting)



"""
The Answer is _____
"""
# def my_function():
#     n = 67
#     # return n + 3
#     print(f"The answer is {n}")
#     return 'something'

# print(my_function()) # Returns 70
# answer = my_function()
# print(answer)


# --- Slide 12 Defining Functions with positional AND keyword parameters
# def add(a, d, b = 4, c = 7):
#     return a + b + c + d
#
# answer = add(a = 1, d = 3) # It will print 14
# print(answer)

"""
IMPORTANT!
POSITIONAL parameters HAVE TO come BEFORE KEYWORD parameters 
"""




# ANOTHER EXAMPLE





# --- Slide 13 Your Turn
"""
Write a function called find_bigger that takes two float values
as parameters and returns the larger of the two. 
"""
# def find_bigger(a, b):
#     if a > b:
#         return a
#     return b
#
# n1 = float(input("Enter a decimal number: "))
# n2 = float(input("Enter another decimal number: "))
# print(find_bigger(n1, n2))








# --- Slide 14 Function Application 1
"""
Write a function called no_ints that accepts a string that may contain letters and/or numbers.
The function returns the string with the digits removed.

For example, if the string is pass123word the return value is password

Hint: Use a string method you learned in the previous chapter
"""
# def no_ints(my_string):
#     new_string = ""
#     for char in my_string:
#         if not char.isdigit():
#             new_string += char
#
#     return new_string
#
# result = no_ints('123hello123')
# print(result)




# --- slide 15 Function Application 2
"""
Write a function called factors that accepts an integer and returns 
a list of its factors (integers divisisble by that number).
"""
# def factors(n):
#     my_factors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             my_factors.append(i)
#
#     return my_factors
#
# result = factors(20)
# print(result)





# --- Slide 18 The Dictionary Data Type
cars =  {} # Empty Dictionary we can add entries to
# print(type(cars))

# cars = {'Ford' : "Fusion", 'Toyota' : 'Camry', 'Jeep': 'Wrangler', 'Tesla' : 'Model 3'}  # Example dictionary of car makes and models

# print(cars[0]) # Can't access dicitony using index ERROR

# print(cars['Ford']) # Prints 'Fusion' -> Value
#
# print(len(cars))
#
# # Dictionary KEYS can be any IMMUTABLE data type (int, string, float, tuple), while VALUES can be of ANY type
# character = {
#     "names": ["Arin", "Luna", "Thorin"],
#     "races": ["Elf", "Human", "Dwarf"],
#     "classes": ["Wizard", "Rogue", "Fighter"],
#     "weapons": ["Staff", "Dagger", "Axe"]
# }
#
# print(character['names'])
# print(character['names'][1])
#
# print(character['weapons'][2])# Print Axe
# character['weapons'].append('whip')
#
# print(character)

"""
What happens if a dictionary key is a mutable type such as a list?
"""
# character = {["Arin", "Luna", "Thorin"] : 'names'} # KEYS HAVE TO BE IMMUTABLE
# character = {("Arin", "Luna", "Thorin") : 'names'}
# print(character)


# ---Slide 19 Your Turn
"""
Weekly Schedule

Create a dictionary to store your weekly activities with: 

    Keys: Tuples containing (day, time) 
    Values: Strings describing the activity 
    Include at least 3 activities

For example, one entry could say: 
	("Mon", "4 PM"): "Soccer Practice"
"""
# my_activities = {("Mon", "4 PM"): "Soccer Practice", ('Wed', 11): "Programming class"}



# --- Slide 20 Dictionaries Are Unordered
cars = {'Ford' : "Fusion", 'Toyota' : 'Camry', 'Jeep': 'Wrangler', 'Tesla' : 'Model 3'}
# cars[1] #This gives an Error because we can't use indexes

# print(cars['Toyota'])  # This is okay because we reference a key

# print(cars['toyota'()]) # Prints ERROR

# print(cars.get('Porche'))



# --- Slide 21 Dictionary Keys Must Be Unique
# fords = {'Ford': 'Mustang', 'Ford': 'Fusion', 'Ford': 'F150'}

# print(fords)  # Only returns ('Ford': 'F150')
# print(len(fords))


# BETTER
# fords = {'Fords': ["Mustang", "Fusion", "F150"]}




# --- Slide 22 Adding and Removing Dictionary Entries
# cars = {'Ford':"Fusion", 'Toyota': "Camry", 'Jeep':"Wrangler"}
# cars["Honda"] = "Accord"
# print(cars)
#
# cars.pop('Toyota')
# print(cars)

# cars.pop("Ferrari") # ERROR
# print(cars)

# if cars.get('Ferrari') != None:
#     cars.pop('Ferrari')
# else:
#     print('Brokey')

"""
Your turn 
    1) Add Chevy Camaro to the list
    2) Remove Jeep Wrangler from the list and print a message saying that it was purchased 
       (Save the pop to a varaible). 
# """
# cars['Chevy'] = 'Camaro'
# print(cars)
#
# new_car_make = input('Enter a car make to remove: ')
# new_car_model = cars.pop(new_car_make)
#
# print(f'You bought a {new_car_make} {new_car_model}')

# --- Slide 23 Getting all keys and values in a dictionary
characters = {
    "warrior": ("HP", 100),
    "wizard": ("HP", 60),
    "archer": ("HP", 80),
    "rogue": ("HP", 65),
    "paladin": ("HP", 110),
    "bard": ("HP", 55),
    "ranger": ("HP", 75)
}

print(characters.keys()) # Use the .keys method to see all the .keys in a given dictionary

print(characters.values())  # Use the .values method to see all the values in a given dictionary

print(characters.items())  # Use the .items method to see all the key-value pairs in a dictionary as tuples

# --- Slide 24 Looping over dictionary entries
for key in characters.keys():
    # print(key)
    if key == 'archer':
        print("Boom you shot an arrow")


for value in characters.values():
    print(value[1])


for both in characters.items():
    print(both[0], both[1][1])

for k, v in characters.items():
    print(k, v[1])

# --- Slide 25 You Try 1
"""
Given the dictionary below, each key represents a character class.

Each value is a tuple containing "HP" and the character's health.

Use a for loop and conditional to print the class (key) of every character class whose HP is greater than 70.
"""
characters = {
    "warrior": ("HP", 100),
    "wizard": ("HP", 60),
    "archer": ("HP", 80),
    "rogue": ("HP", 65),
    "paladin": ("HP", 110),
    "bard": ("HP", 55),
    "ranger": ("HP", 75)
}

for value in characters.values():
    # print(value)
    if value[1] > 70:
        print(value)
        # PROBLEM: YOU LOSE KEYS

for key, value in characters.items():
    if value[1] > 70:
        print(key)




# --- Slide 26 You Try 2
"""
Given lists l1, and l2 below, create a dictionary where for each entry the key is the elements in the first list 
and the values are the elements in the second list. 

For example, one of your dictionary entries would be ‘a’:1
"""

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]







# --- Slide 30 Writing Text to a file
pass  # Open file in write mode

pass  # Write first record and start a new line
pass  # Write second record and start a new line
pass  # Write final record

pass  # Close the file





# --- Slide 33 Writing Numbers to a file






# --- Slide 34 Reading Text from a file



pass  # Writes each line into a list
pass




pass  # Individually show each score that is read




# --- Slide 36 Parsing data from a file
# f = open("myfile.txt", "r")
# lines = f.readlines()
# f.close()



# for line in lines:
pass
pass  # Separate name and score using the colon (:) as the seperator character
pass  # First item is the name
pass  # Convert score to an integer

    #DEBUG INFO
pass  # Add score to running total
pass

pass  # Calculate class average




# --- Slide 37  You try
"""
Modify the myfile.txt program created earlier program to identify the student with the highest score.

    Print the name of the student and the score 
"""
# f = open("myfile.txt", "r")
# lines = f.readlines()
# f.close()
#
#


# --- Slide 38 OS Module
"""
    Place-holder for future code
"""