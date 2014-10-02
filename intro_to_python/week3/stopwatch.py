# "Stopwatch: The Game"
__author__ = "mamaray"

import simplegui


# define global variables
time = 0
num_stops = 0
num_cool_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(number):
    # Number is in deci-seconds
    num_tot_seconds = number // 10
    num_mins = num_tot_seconds // 60
    num_seconds = num_tot_seconds % 60
    num_deci = number % 10
    
    # format and return string
    output = "%0d:%02d.%d" % (num_mins, num_seconds, num_deci)
    return output


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

    
def stop():
    global num_stops, num_cool_stops
    if timer.is_running() == True:
        timer.stop()
        num_stops += 1
        if time % 10 == 0:
            num_cool_stops += 1
   
    
def reset():
    global time, num_stops, num_cool_stops
    timer.stop()
    time = 0
    num_stops = 0
    num_cool_stops = 0

    
# define event handler for timer with 0.1 sec interval
def update():
    global time
    time += 1

    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [50,100], 48, "White")
    canvas.draw_text(str(num_cool_stops)+"/"+str(num_stops)
                     , [150,20], 24, "Red")

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)


# register event handlers
timer = simplegui.create_timer(100, update)


# start frame
frame.start()

