# implementation of card game - Memory
__author__ = "mamaray"

import simplegui
import random

tiles, exposed = [], []
state, pick1, pick2, turns = 0, 0, 0, 0

# helper function to initialize globals
def new_game():
    # make new tiles and reset the views
    global tiles, exposed, state, pick1, pick2, turns
    
    tiles = range(1, 9) + range(1, 9)
    random.shuffle(tiles)
    exposed = [False] * 16
    state, pick1, pick2, turns = 0, 0, 0, 0
     
# define event handlers
def mouseclick(pos):
    global exposed, state, pick1, pick2, turns
    
    # which tile did we click on?
    tile_num = pos[0] // 50        
    
    # no-op if tile already showing or disabled
    if exposed[tile_num] == True:
        return
    else:
        exposed[tile_num] = True
    
    # start of the game, 1 card shows    
    if state == 0:
        state = 1
        pick1 = tile_num
    # 2 cards show
    elif state == 1:
        state = 2
        pick2 = tile_num
        turns += 1
    # 3rd pick, back to 2 cards show
    else:
        state = 1
        if tiles[pick1] != tiles[pick2]:
            exposed[pick1] = False
            exposed[pick2] = False
        
        pick1 = tile_num
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # update the score
    label.set_text("Turns = "+str(turns))

    # draw lines to give the illusion of boxes    
    for i in range(1, 16):
        canvas.draw_line((50 * i, 0), (50 * i, 100), 1, 'White')
    
    # draw the "tiles" if we should
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text(str(tiles[i]), (15 + 50 * i, 60), 30, 'Orange')
      

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
