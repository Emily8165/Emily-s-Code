# CREATE ROCK PAPER SISSORS GAME TO PLAY AGAINST THE COMPUTER - intermediate
import random
import time

opening = ("lets play a game of rock paper sissors, hit enter when you are ready:)")
countdown = ["ready...", "rock...", "paper...", "sissors...", "Shoot!!!"]
choices = ("rock", "paper", "sissors")
error = ("Error!: That is not a valid response please try again")


def RCP():
    print(input(opening))
    def intro():
        countdown = ["ready...", "rock...", "paper...", "sissors...", "Shoot!!!"]
        for z in range(5):
            print(countdown[0])
            countdown.pop(0)
            time.sleep(1)
        return(countdown)    
    intro()   
    def main():
        x = input()
        while True:
            if opening in (choices):
                print(error)
                RCP()
            else:
                break
        cx = random.choice(choices)
        print(cx)
        def compwin():
            z = input("I win! would you like to play again? y/n: ")
            if z == "y":
                RCP()
            elif z == "n":
                print("Play again soon!")
            else:
                print(error)
                compwin()
        def usewin():
            z = input("You win! would you like to play again? y/n: ")
            if z == "y":
                RCP()
            elif z == "n":
                print("Play again soon!")
            else:
                print(error)
                usewin()
        if x == cx:
            return(main())
        elif x == "rock" and cx == "paper":
            return(compwin())
        elif x == "paper" and cx == "sissors":
            return(compwin())
        elif x == "sissors" and cx == "rock":
            return(compwin())
        else:
            usewin()    
    main()
RCP()

