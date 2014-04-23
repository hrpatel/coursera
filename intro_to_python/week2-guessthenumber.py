# template for "Guess the number" mini-project
__author__ = "hrpatel"

import simplegui
import random
import math


# initialize global variables used in your code
range = 100
num_to_guess = -1
num_guesses = -1
text_box = -1

# helper function to start and restart the game
def new_game(new_range):
    global range, num_guesses, num_to_guess
    range = new_range
    num_guesses = int(math.log(new_range, 2) + 1)
    num_to_guess = random.randint(0,range)
    
    print
    print "New game. Guess a number between 1 and %d." % range
    print "You have %d guesses remaining" % num_guesses
    
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    new_game(100)

    
def range1000():
    # button that changes range to range [0,1000) and restarts
    new_game(1000)
    
    
def input_guess(guess):
    global num_guesses
    
    text_box.set_text("")
    
    # main game logic goes here	
    your_guess = int(guess)
    print "Your guessed:", your_guess
    if your_guess == num_to_guess:
        print "You win!"
        new_game(range)
        return
    elif your_guess > num_to_guess:
        print "Lower"
    else:
        print "Higher"
    print 
    
    if num_guesses == 1:
        print "You're out of guesses!"
        new_game(range)
        return
    else:
        # decrement number of guesses
        num_guesses -= 1
        print "You have %d guesses remaining" % num_guesses
        
        
# create frame
frame = simplegui.create_frame("Guess the Number!", 100, 200)


# register event handlers for control elements
frame.add_button("New Game: 100", range100)
frame.add_button("New Game: 1000", range1000)
text_box = frame.add_input("Enter your guess:", input_guess, 100)


# call new_game and start frame
new_game(range)
frame.start()


# always remember to check your completed program against the grading rubric
