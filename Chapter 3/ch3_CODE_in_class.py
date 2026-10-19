"""
Chapter 3 key skills

In this chapter, we learn how to:
    - Understand how libraries, modules, and packages extend Python programs.

    - Import modules and specific functions, including using the random module
      to create simulations and games.

    - Work with characters using their numeric values with ord() and chr().

    - Treat strings as data structures and use len() to determine their size.

    - Access and process string characters using positive and negative indexing.

    - Loop through strings using both indexes and individual characters.

    - Create substrings using slicing with start, stop, and step values.

    - Manipulate and test strings using common string methods.

    - Search strings for characters and substrings and use Boolean flags
      to track whether conditions have been met.

    - Understand the difference between mutable and immutable data.

    - Create, index, and work with lists, including nested lists.

    - Add, replace, and remove list elements using common list methods.

    - Build and filter lists using loops and conditional statements.

    - Process list data using functions such as len(), min(), max(), sum(),
      and count().

    - Sort lists and understand the difference between sort() and sorted().
"""


# --- Slide 6 (Importing Libraries - Random)
"""
There are three ways to import a library or module

Let's look at all three by generating a random number between 1 and 10 using randint
"""

# 1) Import everything organized in a 'toolbox'

# import random
# n = random.randint(1,10)
# print(n)

"""
In order to use randint (or any function from the random library we have to first reference the library the function is from.
This is similar to knowing which 'toolbox' you are grabbing a specific tool (or function) from
"""

# 2) Import everything dumping out all the tools

# from random import *
# n = randint(1,10)
# print(n)


"""
Here we do NOT have to reference the toolbox because all our tools are now 'dumped out'.

What actually happens is memory references are created in your program to the functions from the module imported

This is usually not the best practice because:
    1) It makes programs slightly longer to contain extra memory (not a big issue) 
    2) Can accidently overide a function by declaring a variable with the same name as the function (bigger issue) 
"""

# 3) Import a specific tool from the toolbox

# from random import randint, random
#
# print(random())
#
# n = randint(1,10)

"""
Here we only import one function from the 26 or so available in the random module. 

Even though we call randint to use it without the random keyword, if we did use randint as a variable, Python
separates the name of the variable and the name of the function into two completely separate memory locations. 
"""

# --- Slide 7 (Dice Rolling Simulator)
# from random import randint
#
# rolls = 10
# sides = 6
#
# for i in range(rolls):
#     result = randint(1,sides)
#     print(result)


# --- Slide 8 (Guess the number Game)
# from random import randint
#
# computer_num = randint(1,100)
# player_guess = 0
#
# while computer_num != player_guess:
#     player_guess = int(input("Please enter a number between 1 and 100: "))
#
#     if player_guess == computer_num:
#         print("You are correct!")
#
#     elif player_guess > computer_num:
#         print("Try again, you guesses HIGH.")
#
#     elif player_guess < computer_num:
#         print("Try again, you guesses LOW.")

############################################################
# In-class coin flip simulator (mote carlo simulation)

from random import randint

# simulation = 10000
# sum_of_flips = 0
#
#
#
# for i in range(simulation):
#
#     head_count = 0
#     flip_count = 0
#
#     while head_count < 3:
#         flip_count +=1
#         flip_result = randint(0,1)
#         # print(flip_result)
#
#         if flip_result == 0:
#             head_count +=1
#
#         else:
#             head_count = 0
#
#     sum_of_flips += flip_count
#     print(f"It took you {flip_count} to get 3 heads in a row")

# print(f"It took an average of {sum_of_flips/simulation} to get three heads in a row over {simulation} simulations.")
############################################################


# --- Slide 9 Characters
# print('A' < 'a')
#
# print(ord('a'))
# print(chr(97))


# --- Slide 10 Characters
"""
Creating a simple Ceaser Cipher
"""
# letter = input("Enter a letter: ")
# shift = int(input("Enter a shift: "))
#
# new_ASCII = ord(letter) + shift
# new_letter = chr(new_ASCII)
# print(new_letter)



# --- Slide 11 Strings - length
message = "hello"
longer_message = "How are you doing today?"

# print(len(message))
# print(len(longer_message))




# --- Slide 12 Strings - Indexing
# print(message[1]) # This prints letter 'e'
# print(message[0]) # This prints letter 'h'

# print(message[5]) # This give an IndexError

# --- Slide 13 Strings - Indexing
# print(message[-1]) # This prints the LAST character 'o'
# print(message[-2])



#Slide 14 Strings - Looping
"""
Two ways to loop - 
 1) Using an index 
 2) Using the characters in the string
"""

# for i in range(len(message)):
#         print(i, message[i])
#
# for c in message:
#     print(c)
#
# for i,c in enumerate(message):
#     print(message[i], c)

#--- Slide 15 Your Turn
pass




# --- Slide 17 Slicing for substrings
# some_string = 'The quick brown fox jumped over the lazy dog'
#
# print(some_string[0:]) # The whole message
# print(some_string[4:]) # Start at character 4 and go till end
#
#
# print(some_string[4:9]) # Start at character 4 and go till 8
# print(some_string[4:len(some_string)]) # Char 4 till end
#
#
# print(some_string[-3:]) # Third to last char until end
# print(some_string[-8:-4]) # 8'th to last char until 5 to last
#
# print(some_string[::2]) # Entire string but only every other character displayed
# print(some_string[::-1]) # Entire Sting Backwards
#
# print(some_string[0:3] + some_string[-4:]) # Combine slices (Prints 'The dog')
#

# --- Slide 18 Your turn - Move Two Letters
# word = input("Please enter a word:")
#
# new_word = word[-2:] + word[:-2]
# print(new_word)



# --- Slide 20 String Methods
# superhero = 'the incredible hulk'
#
# print((superhero.upper()))
# print(superhero.title())
# print(superhero.lower())
# print(superhero.count('h'))

# print(superhero[0:4].upper() + superhero[5:])
# print(superhero.upper)


# --- Slide 21 String Methods
address = '123 Fake St.'

# print(address.isdigit()) # Is the whole string a string of digits?
# print(address.isupper())

# Check which characters are digits
# for char in address:
#     print(char, char.isdigit())

# Check which characters are uppercase
# for char in address:
#     print(char, char.isupper())

# Check which characters are lowercase
# for char in address:
#     print(char,char.isalnum())


########## In class exercise (string methods) ############################
"""

Ask the user for an input string.

The program should:
    1) Count and display how many lower-case letters the string has
    2) print a new string that only contains the uppercase letters from the string the user entered.


For example:
    If the user enters: 'The Quick Brown Fox Jumped Over the Lazy Dog'
        1) The lower-case letter count would be 12
        2) The string printed should be: 'TQBFJOLD'

                Since those are the capital letters in the first string
"""
# message = input("Please enter a string: ")
# lower_case = 0
# only_uppercase = ""
# word_count = 0
#
# for char in message:
#     # print(char)
#     if char.isupper():
#         # print(char)
#         only_uppercase +=char
#     if char.islower():
#         lower_case +=1
#     if char == ' ':
#         word_count+=1
#
# print(only_uppercase)
# print(f"You have {lower_case} lower case letters.")
# print(f'You have {word_count+1} words')



####################################################################################


# --- Slide 22 String Methods - split
# story = "A long time ago in a galaxy far far away."
#
# words = story.split()
# print(words)
#
# print(words[1].upper()) # long


# --- Slide 23 Testing for a Substring
text = """A long time ago in a galaxy far far away..
It is a period of civil war.
Rebel spaceships, striking
from a hidden base, have won
their first victory against
the evil Galactic Empire."""


# print('time' in text) # True
# print('galactic' in text) # False

# print('galactic' in text.casefold()) #TRUE
#
# print(text.index('time')) # Tells you the position of the first letter in the word
#
# print(text.index('Time')) # ERROR because string (Time) does not exist


# --- Slide 24 - Boolean Flags
"""Check if a string has the letter A"""
# while True:
#     my_string = input("Please enter a string: ")
#
#     #set flags
#     has_A = False
#
#     for c in my_string:
#         if c == 'A':
#             has_A = True
#
#     if has_A:
#         print("You have an A in your string")
#         break
#     else:
#         print('No A in your string, try again.')



# --- Slide 26 Mutable vs. Immutable Data
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0])

# mutable[0] = 'H'
# mutable[2] = 'hello'
# print(mutable)

# immutable = 'Good'
# print(immutable)
# print(immutable[0]) #This command is fine

# immutable[0] = 'H' # ..This is not. Can't override the individuals characters
# immutable = 'Hood' #...But you can override the variable itself
# print(immutable)




# --- Slide 28 Declaring Lists
my_list = []
print(type(my_list))
print(len(my_list))



fruits = ['apple', 'orange', 'kiwi'] # Three element list
profile = ['Jon', 30, True, [1.5, 3]] # Lists can mix data types

coordinates = [[-1,3], [3,0], [2.5, -1.6]] # Lists can contain other lists
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1][0]) # prints 3



# --- Lists can store the result of other operation
# x = 19
#
# def hello():
#     return 'hi'
#
# lst = [x, x**0.5, x+1, hello()]
# print(lst)


# --- Slide 29 Your turn
pass



# --- Slide 30 Adding Elements to a list
pokemon = ["Pikachu", "Eevee", "Charmander", "Squirtle"]

## 1) Using the ‘append’ method (most common)
    ## Adds the element to the end of a list
# pokemon.append('Rowlet')
# print(pokemon)


## 2) Using the .insert method
    ## Adds the element at the index specified
# pokemon.insert(1, 'Snoralax')
# print(pokemon)


## 3) Using the .extend method
    ## Adds the elements of the first list to the second to create a combined list
# new_pokemon = ['Articuno', 'Zapdos', 'Moltres']
#
# pokemon.extend(new_pokemon)
# print(pokemon)



# --- Slide 31 Application - Adding to a list by looping
roster_size = int(input("Enter the number of people to add: ")) #Get input about number
roster_lst = [] #Create an empty list to hold the people

for i in range(roster_size): #Loop through however many people we said we wanted to add
    new_member = input("What is the person's name: ") #Get the persons name
    roster_lst.append(new_member) #Add the person to the end of the roster list

print(roster_lst) # print results


# --- Slide 32 Application – Filtering a list
people = ['Jack', 'Frank', 'Macy', 'Nancy', 'Bill']

revised_people = []

pass


# --- Slide 33 Whole list operations
# from random import randint
# lst = []
# for i in range(10):
#     lst.append(randint(1, 100))
#
# print(lst)

pass


# --- Slide 34 Skill Review – Getting Input until break
##Stopping a loop when the 'enter' key is pressed.
pass




# --- Slide 36 Replacing and Removing Elements
lst= [1,2,3,4]
pass



# --- Slide 37 Manipulating List Elements With Loops
"""
Square each integer in the list and overwrite the original in that position
"""
numbers = [2,3,4,5]
pass


"""
Remove the space character and capitalize the first letter of each name
"""
names = ["  alice", "bob  ", "  charlie  "]
cleaned_names = []

pass




# --- Slide 38 Sorting
high_NFL_scores = [99, 101, 95, 113, 98, 96, 105, 101, 97, 103, 95, 106, 99, 98, 96]
"""
We can use <list>.sort() to re-order the original list in order.
By default, it sorts the list from low to high. 

This is called sort-in-place because it changes the original lsit so we cannot reference it in the original (unsorted) way anymore
"""
pass



"""
Comment out the sort method above to compare.

Notice that if we use the sorted() method, we get the orignal list with nothing sorted. 

This happens because sorted() returns a NEW list that is sorted, leaving the orignal one intact. 
In order to see it we need to save it to a variable.
"""
pass


pass


"""
To sort in reverse we can add the 'reverse' parameter to our command. This works with both methods. 
"""
pass


# --- Slide 39 Searching and Filtering
# high_NFL_scores = [99, 101, 95, 113, 98, 96, 105, 101, 97, 103, 95, 106, 99, 98, 96]
# high_NFL_scores.sort(reverse=True)

"""
Task 1:
Create a new list with only scores that are 100 or more
"""
pass


"""
Task 2:
Create a new list that has elements that show up at least twice on the original list 
"""
pass

