## 7a q1

class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def translate(self, deltax = 0, deltay = 0):
        """Translate the point in the x direction by deltax
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

        
point = Point2D(3, 9)
point.translate(5, -2)
 
#Point2D(3, 9)
#Point2D.translate(5, -2)
 
point1 = Point2D(3, 9)
point2 = Point2D()
point2.translate(20, 4)
 
#Point2D = (3, 9)
#point2D.translate(5, -2)


## q2

point0 = Point2D(2, 5)
point1 = Point2D(8, 3)
point2 = Point2D(0, 2)
points = [point0, point1, point2]
#points.translate(-1, -1)
 
    
point0 = Point2D(2, 5)
point1 = Point2D(8, 3)
point2 = Point2D(0, 2)
points = [point0, point1, point2]
for point in points:
    point.translate(-1, -1)
 
points = [(2, 5), (8, 3), (0, 2)]
for point in points:
    #point.translate(-1, -1)
    pass
    
    
    
## q3
point = Point2D(3, 6)
s = str(point)
 
point = Point2D(3, 6)
s = str(point)
#newpoint = Point(s)
 
point = Point2D(3, 6)
#lst = list(point)
 
point = Point2D(3, 6)
#lst = list(point)
#x = lst[0]



## q 7
i = 500
for x in range(77):
    i = i * .9 + 10
    print i

