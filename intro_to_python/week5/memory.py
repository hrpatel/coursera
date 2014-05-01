# implementation of card game - Memory
__author__ = "mamaray"

import simplegui
import random


# helper function to initialize globals
def new_game():
    global game_nums, hide_tile, disable_tile
    game_nums = range(1, 9) + range(1, 9)
    random.shuffle(game_nums)
    show_hide = [1] * 16
    disable_tile = [1] * 16
     
# define event handlers
def mouseclick(pos):
    # which tile did we click on
    tile_num = pos[0] // 50
    
    # invert the tile
    if hide_tile[tile_num] == 0:
        hide_tile[tile_num] = 1
    else:
        hide_tile[tile_num] = 0
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # draw the lines to give the illusion of boxes    
    for i in range(1, 16):
        canvas.draw_line((50 * i, 0), (50 * i, 100), 1, 'White')
    
    # draw the "tiles" if we should
    for i in range(16):
        if hide_tile[i] == 1 or disable_tile[i] == 1:
            canvas.draw_text(str(game_nums[i]), (15 + 50 * i, 60), 30, 'Orange')
        

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


# Always remember to review the grading rubric
