## quiz 7b q7

SCREEN_SIZE=[10,10]
p = [1,2]
v = [3,4]

def move(position, vector):
    position = [(pos + vec) % size for pos in position for vec in vector for size in SCREEN_SIZE]
    
print p, v    
for i in range(10):
    move(p,v)
    print p, v    
print
print

    

def move_dimension(dimension, position, vector):
    """Moves the position component by the given vector component in 1D toroidal space."""
    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]

def move2(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    move_dimension(0, position, vector)
    move_dimension(1, position, vector)
    
print p, v    
for i in range(10):
    move2(p,v)
    print p, v    
