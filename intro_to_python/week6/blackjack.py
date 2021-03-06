# Mini-project #6 - Blackjack
__author__ = "mamaray"


import simplegui
import random


# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    


# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = [0, 0] # [wins, loses]
DECK = None
player_h = None
dealer_h = None


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.values = []

    def __str__(self):
        return_val = "Hand contains"
        for card in self.cards:
            return_val = return_val + " " + str(card)
        return return_val

    def add_card(self, card):
        self.cards.append(card)
        self.values.append(VALUES[card.get_rank()])

    def get_value(self):
        # compute the value of the hand
        value = sum(self.values)
        for card_val in self.values:
            if (value + 10) < 22 and card_val == 1:
                value += 10
        return value
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 90
        
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
    
    def __str__(self):
        return_val = ""
        for card in self.cards:
            return_val = return_val + " " + str(card)
        return return_val


#define event handlers for buttons
def deal():
    global outcome, in_play, DECK, player_h, dealer_h, score

    # game on!
    if in_play:
        score[1] += 1
    else:
        in_play = True

    print 
    print "New Game!"
    outcome = "Hit or Stand?"
    
    # create and shuffle the deck
    DECK = Deck()
    DECK.shuffle()
    
    # Deal for player
    player_h = Hand()
    player_h.add_card(DECK.deal_card())
    player_h.add_card(DECK.deal_card())
    print "Player has: " + str(player_h)
    
    # Deal for dealer
    dealer_h = Hand()
    dealer_h.add_card(DECK.deal_card())
    dealer_h.add_card(DECK.deal_card())
    print "Dealer has: " + str(dealer_h)
    

def hit():
    global in_play, score, outcome
    
    # if the hand is in play, hit the player
    if in_play and player_h.get_value() <= 21:
        player_h.add_card(DECK.deal_card())
        print "Player hits"
        print str(player_h) + ":", str(player_h.get_value()), "points"

        # if busted, assign a message to outcome, update in_play and score
        if player_h.get_value() > 21:
            print "Player has busted!"
            outcome = "Player has busted! New game?"
            in_play = False
            score[1] += 1
        
       
def stand():
    global in_play, score, outcome
    
    if in_play:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_h.get_value() < 17: 
            dealer_h.add_card(DECK.deal_card())
            print "Dealer hits"
            print str(dealer_h) + ":", str(dealer_h.get_value()), "points"
    
        # if busted, assign a message to outcome, update in_play and score
        if dealer_h.get_value() > 21:
            print "Dealer has busted!"
            print "Player Wins!"
            outcome = "Player Wins! New deal?"
            score[0] += 1
        elif dealer_h.get_value() >= player_h.get_value():
            print "Dealer Wins!"
            outcome = "Dealer Wins! New deal?"
            score[1] += 1
        else:
            print "Player Wins!"
            outcome = "Player Wins! New deal?"
            score[0] += 1
        
        in_play = False

        
# draw handler    
def draw(canvas):
    # draw the cards
    dealer_h.draw(canvas, [50, 150])
    player_h.draw(canvas, [50, 350])
    
    # draw text on the table
    canvas.draw_text('Blackjack', (420, 580), 40, 'White', 'sans-serif')
    canvas.draw_text('Dealer', (50, 100), 25, 'Orange', 'sans-serif')
    canvas.draw_text('Player', (50, 500), 25, 'Orange', 'sans-serif')
    canvas.draw_text('Wins: ' + str(score[0]) + " Loses: " + str(score[1]), (50, 520), 18, 'Orange', 'sans-serif')
    canvas.draw_text(str(outcome), (50, 300), 20, 'Yellow', 'sans-serif')
    
    # hide dealers pot card
    if in_play:
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], 
                    CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [51 + CARD_BACK_CENTER[0], 151 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")


#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
