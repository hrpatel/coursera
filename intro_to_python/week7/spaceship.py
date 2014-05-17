# program template for Spaceship
import simplegui
import math
import random

__author__ = "mamaray" 

# globals for user interface
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = [WIDTH, HEIGHT]
DIMENSION = 2

ang_vel = 3
lives = 3
score = 0
time = 0.5
turn_dir = {37: -1, 39: 1}


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.ogg")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.ogg")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


def deg_to_rad(angle):
    return angle * math.pi / 180


def keydown_handler(key):
    # change ship direction 
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]:
        my_ship.turn(turn_dir[key])
        return
    
    # start ship thrusters
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thruster(True)
        return
    
    # fire missles
    if key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        return

    
def keyup_handler(key):
    # stop rotating the ship
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]:
        my_ship.turn(0)
        return
    
    # stop the thrusters
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thruster(False)
        return
    
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.fwd_vec = angle_to_vector(self.angle)
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        # draw the ship
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, deg_to_rad(self.angle))

    def shoot(self):
        global a_missile

        # calculate missle position and velocity        
        missle_pos, missle_vel = [0, 0], [0, 0]
        for i in range(DIMENSION):
            missle_pos[i] = self.pos[i] + self.radius * self.fwd_vec[i]
            missle_vel[i] = self.vel[i] + self.fwd_vec[i] * 2.75

        # fire missle
        a_missile = Sprite(missle_pos, missle_vel, self.angle, 
                           0, missile_image, missile_info, missile_sound)
        
    def update(self):
        # update the direction ship faces
        self.angle += self.angle_vel
        self.fwd_vec = angle_to_vector(deg_to_rad(self.angle))
        
        for i in range(DIMENSION):
            # calculate acceleration vector
            if self.thrust:
                self.vel[i] += self.fwd_vec[i] * 0.5

            # set the new position            
            self.pos[i] = (self.pos[i] + self.vel[i]) % SCREEN_SIZE[i]

            # slow down and stop eventually
            self.vel[i] *= 0.94
            
    def turn(self, direction):
        # set angular velocity
        self.angle_vel = direction * ang_vel
    
    def thruster(self, on_off):
        # set the thruster on/off
        self.thrust = on_off
        
        if on_off:
            # draw ship with thrusters
            self.image_center[0] = 135
            ship_thrust_sound.play()
        else:
            # draw ship without thrusters
            self.image_center[0] = 45
            ship_thrust_sound.rewind()

            
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        # draw sprite object
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, deg_to_rad(self.angle))
    
    def update(self):
        # rotate the object
        self.angle += self.angle_vel

        # update position
        for i in range(DIMENSION):
            self.pos[i] = (self.pos[i] + self.vel[i]) % SCREEN_SIZE[i]

            
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # score and lives labels
    canvas.draw_text('Lives: ' + str(lives), (30, 50), 25, 'Orange', 'sans-serif')
    canvas.draw_text('Score: ' + str(score), (WIDTH - 125, 50), 25, 'Orange', 'sans-serif')

    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)], 
                    [random.randrange(-1, 2) * 1.5, random.randrange(-1, 2) * 1.5], 
                    deg_to_rad(random.randrange(360)), 
                    random.choice([-1, 1]) * 2, 
                    asteroid_image, asteroid_info)


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)


# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
my_ship.shoot()
rock_spawner()


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
