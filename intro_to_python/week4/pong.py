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

# initialize ball properties
ball_pos = [0, 0]
ball_vel = list(ball_pos)

# initialize paddle properties
paddle1_pos = [ [0, 0], [0, 0] ]
paddle2_pos = list(paddle1_pos)
paddle1_vel, paddle2_vel = 0, 0

# initialize score
score1, score2 = 0, 0


# make the game more interesting
def make_interesting():
    global ball_pos
    how_interesting = 1.05
    ball_vel[0] *= how_interesting
    ball_vel[1] *= how_interesting

    
# stop paddles from leaving the screen
def move_paddle(pad, vel):
    pad[0][1] += vel
    pad[1][1] += vel

    if pad[0][1] <= 0:
        pad[0][1] = 0
        pad[1][1] = PAD_HEIGHT
        
    if pad[1][1] >= HEIGHT:
        pad[0][1] = HEIGHT - PAD_HEIGHT
        pad[1][1] = HEIGHT


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [-1 * random.randrange(3, 6), random.randrange(3, 6)]
    else:
        ball_vel = [random.randrange(3, 6), -1 * random.randrange(3, 6)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    # initialize paddle
    paddle1_pos = [[WIDTH - HALF_PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT], 
                   [WIDTH - HALF_PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]
    paddle2_pos = [[0 + HALF_PAD_WIDTH -1 , (HEIGHT / 2) - HALF_PAD_HEIGHT], 
                   [0 + HALF_PAD_WIDTH - 1, (HEIGHT / 2) + HALF_PAD_HEIGHT] ]

    paddle1_vel, paddle2_vel = 0, 0

    # initialize score
    score1, score2 = 0, 0
    
    # pick a random direction to start with
    spawn_ball(random.randint(0, 1))
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # collide and reflect off of left side
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos[0][1] and ball_pos[1] <= paddle2_pos[1][1]:
            ball_vel[0] = - ball_vel[0]
            make_interesting()
        else:
            spawn_ball(LEFT)
            score2 += 1
    
    # collide and reflect off of right side
    if ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle1_pos[0][1] and ball_pos[1] <= paddle1_pos[1][1]:
            ball_vel[0] = - ball_vel[0]
            make_interesting()
        else:
            spawn_ball(RIGHT)
            score1 += 1
    
    # collide and reflect off the top/bottom wall
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # move the ball
    ball_pos[0] += ball_vel[0]        
    ball_pos[1] += ball_vel[1]        

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Brown", "Red")
    
    # update paddle's vertical position, keep paddle on the screen
    move_paddle(paddle1_pos, paddle1_vel)
    move_paddle(paddle2_pos, paddle2_vel)
    
    # draw paddles
    canvas.draw_line( paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "Orange")
    canvas.draw_line( paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "Orange")
    
    # draw scores
    canvas.draw_text("P1: " + str(score1), (125, 50), 30, "White")
    canvas.draw_text("P2: " + str(score2), (WIDTH-175, 50), 30, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    velocity_factor = 5
    # P1 uses up/down keys
    # P2 uses 'w'/'s' keys
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = -1 * velocity_factor
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 1 * velocity_factor
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel = -1 * velocity_factor
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 1 * velocity_factor
   
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
frame.add_button("Reset", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
