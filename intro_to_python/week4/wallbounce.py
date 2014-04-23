import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-60.0 / 50.0,  30.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
    
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        vel[0] = - vel[0]
    
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        vel[1] = - vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    global vel
    if key == simplegui.KEY_MAP["down"]:
        vel[0] *= 0.8
        vel[1] *= 0.8
    elif key == simplegui.KEY_MAP["up"]:
        vel[0] *= 1.2
        vel[1] *= 1.2

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
