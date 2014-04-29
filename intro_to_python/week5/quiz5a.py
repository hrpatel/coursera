__author__ = "mamaray"

print range(2, 15, 3)
print range(2, 14, 3)
print range(15, 2, -3)
print range(14, 2, -3)
print 
print


def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers) - 1):
        if numbers[i+1] < numbers[i]:
            return False
    return True
print is_ascending([2, 6, 9, 12, 400])
print is_ascending([4, 8, 2, 13])
print
print


def reverse_string(s):
    """Returns the reversal of the given string."""
    result = ""
    for char in s:
        result = char + result
    return result

print reverse_string("hello")
print 
print


import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point)
    return points

print starting_points(["bob", "alice"])
print 
print


fib = [0,1]
print fib + [2,3]
for i in range(40):
    fib.extend([fib[-2] + fib[-1]])
print fib[-1]
