# Mini-project #6 - Blackjack

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
outcome = ""
score = 0

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
        #print card_loc
        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("D", "K")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.set_draw_handler(draw)


# get things rolling
frame.start()




## q5
l = [[1,2], [3], [4, 5, 6], [7]]

def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result


def list_extend_many2(lists):
    result = []
    for i in range(len(lists)):
        result.extend(lists[i])
    return result


def list_extend_many3(lists):
    result = []
    i = len(lists)
    while i >= 0:
        i -= 1
        result.extend(lists[i])
    return result


def list_extend_many4(lists):
    result = []
    for i in range(len(lists) - 1, -1, -1):
        result.extend(lists[i])
    return result


def list_extend_many5(lists):
    result = []
    i = 0
    while i < len(lists): 
        result.extend(lists[i])
        i += 1
    return result


print list_extend_many(l) 
print list_extend_many2(l) 
print list_extend_many3(l) 
print list_extend_many4(l) 
print list_extend_many5(l) 
print
print

## q6

#n = 127834876
#while n >= 0:
    # Assume this doesn't modify n.
#    n //= 2
#    print n
    

## q7
def results(n):
    numbers = range(2,n)
    results = []
    while len(numbers) > 0:
        popped = numbers.pop(0)
        results.append(popped)
        for i in numbers:
            if i % popped == 0:
                numbers.remove(i)
    return results

print results(10)
print len(results(100))
print len(results(1000))
print
print


## q8
y=1
slow = 1000
fast = 1
print "y: %2d, s: %.4f, f: %.4f"% (y, slow, fast)
while fast < slow:
    slow = (slow * 2) * 0.6
    fast = (fast * 2) * 0.7
    y += 1
    print "y: %2d, s: %.4f, f: %.4f"% (y, slow, fast)
print "y: %2d, s: %.4f, f: %.4f"% (y, slow, fast)

