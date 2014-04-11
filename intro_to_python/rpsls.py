# Rock-paper-scissors-lizard-Spock game

# import required modules
import random

def name_to_number(name):
    """
    This function converts move names to numbers 
    """
    
    # convert name to number using if/elif/else
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = -1
        
    return number


def number_to_name(number):
    """
    This function converts move numbers to names 
    """
    
    # convert name to number using if/elif/else
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
        
    return name
    

def rpsls(player_choice): 
    """
    This function determines the winner of rte RPSLS game by 
    checking the rules of the game. 
    
    Computer move is randomly generated each time this function
    is called. 
    """

    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice
        
    # Convert the move to a number and check if its valid
    if name_to_number(player_choice) != -1:
        player_number = name_to_number(player_choice)
    else:
        print "-- Illegal move by player! --"
        return

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + computer_choice

    # compute difference of comp_number and player_number modulo five
    result_number = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if result_number == 0:
        print "Player and computer tie!"
    elif result_number == 1 or result_number == 2:
        print "Player wins!"
    elif result_number == 3 or result_number == 4:
        print "Computer wins!"
        
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# test failure scenario
# rpsls("sword")


