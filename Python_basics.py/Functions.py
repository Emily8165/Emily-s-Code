"""This file is to track everything about Def functions"""
"""Def functions are used to call blocks of code. 
this code is called at the end of the code as seen in the example, make sure to add the ()
"""
import random
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def guessing_game(a, b):# parameters go here
    guess = int(input("guess the right number: "))
    random_number = random.choice(numbers)
    if guess == random_number:
        print("you guessed right!")
    else: 
        print("you guessed wrong, try again!")
    
    return a+b
    
guessing_game(4, 5) #arguments go here. 

"""Functions can also take arguments in their parentecees 
which can be added onto future fucntions, see example,
sometimes argumensts are shorted to args."""

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""A parameters and arguments are the same from a user persepectives. This is information that is passed into a function
However they are different to the function: 
A parameter is the varioable listed inside the
functions parenthesis and is sets the boundaries 
for the arguments. 

An Argumnet is the thing that goes into the paramiter
"""
def add(a, b):
    return a+b

add(5, 4)



