# Implementation of classic arcade game Pong
__author__ = "mamaray"

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 12
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False

# initialize ball
ball_pos = [WIDTH / 2,  HEIGHT/ 2]
ball_vel = [1, 1]

# initialize paddle
paddle1_pos = [ [0, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT],
               [0, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]
paddle2_pos = [ [WIDTH - PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT],
               [WIDTH - PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]
paddle1_vel = 1
paddle2_vel = 1

# initialize score
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [HEIGHT / 2, WIDTH / 2]
    if RIGHT == True:
        ball_vel = [-1, 1]
    else:
        ball_vel = [1, -1]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    # initialize paddle
    paddle1_pos = [ [0, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT],
               [0, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]
    paddle2_pos = [ [WIDTH - PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
               [WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT],
               [WIDTH - PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]
    paddle1_vel = 1
    paddle2_vel = 1

    # initialize score
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # collide and reflect off of left side
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        ball_vel[0] = - ball_vel[0]
        RIGHT = True
        LEFT = not(RIGHT)
    
    # collide and reflect off of right side
    if ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        ball_vel[0] = - ball_vel[0]
        RIGHT = False
        LEFT = not(RIGHT)
    
    # collide and reflect off the top wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # collide and reflect off of the bottom side
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    ball_pos[0] += ball_vel[0]        
    ball_pos[1] += ball_vel[1]        

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Brown", "Red")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 2, "White", "Orange")
    canvas.draw_polygon(paddle2_pos, 2, "White", "Orange")
    
    # draw scores
    canvas.draw_text("P1: " + str(score1), (125, 50), 30, "White")
    canvas.draw_text("P2: " + str(score2), (WIDTH-175, 50), 30, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    # P1 uses up/down keys
    # P2 uses 'w'/'s' keys
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel *= 1
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel *= 1
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel *= 1
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel *= 1
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    # P1 uses up/down keys
    # P2 uses 'w'/'s' keys
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
