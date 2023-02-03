"""this is the file to cover off all learnings to do with If statements"""
'''there are 3 main parts of if statements. 
If is always the first part of the senario, you can only have one if in a senario.
Elif is an alternative for the if statemnts, you can have as many elifs as you want
Else is always the final one, can basically mean if anything else happens do x'''

import random
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
guess = int(input("guess the right single digit number: "))
random_number = random.choice(numbers)
if guess == random_number:
    print("you guessed right!")
elif guess >= 10:
    print("that is out of the number range")
else: 
    print("you guessed wrong, try again!")