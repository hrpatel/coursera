## q2
favorites = { "ab": "blah"}

#favorites{"fruit" : "blackberry"}
#favorites["fruit" = "blackberry"]
favorites["fruit"] = "blackberry"
#favorites["fruit" : "blackberry"]


print favorites
print
print


## q7
my_list = [1,2,3,4,5,6,7,8,9,0]
def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0

print [n for n in my_list if is_even(n)]
print [is_even(number) for number in my_list]
print [number for number in my_list if is_even(number)]
#print [if is_even(number): number for number in my_list]
print
print


## q8
import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image, 
                      [image_size[0] / 2, image_size[1] / 2],image_size,
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

frame.start()


## q9
import simplegui

frame_size = [400, 400]
image_size = [1521, 1818]

def draw(canvas):
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image, 
                      [220, 100],[100,100],
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

frame.start()


