#ROCK PAPER SCISSORS - simple

import random

choices = ('rock', 'paper', 'scissors')

def RCP():
    x = input("lets play rock paper scissors! Please input rock paper or scissors: ")
    y = random.choice(choices)
    if x == y:
        print("shoot!")
        RCP()
    elif (x == "rock" and y == "scissors") or (x == "scissors" and y == "paper") or (x == "paper" and y == "rock"):
        print("you win!")
    else:
        print("you loose")
RCP()
        