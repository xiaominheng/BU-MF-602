# 
# a1task2.py - Assignment 1, Task 2
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Functions with numeric inputs
# 
#

import math

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def cube(x):
    """ returns the cube of its input
        input x: any number (int or float)
    """
    return pow(x, 3)

# function 2
def slope(x1, y1, x2, y2):
    """ returns the slope of the line formed by two points
        input x1: first point's x-coordinate
        input y1: first point's y-coordinate
        input x2: second point's x-coordinate
        input y2: second point's y-coordinate
    """
    return (y2 - y1) / (x2 - x1)

# function 3
def cylinder_volume(diameter, height):
    """ returns the volumn of cylinder given the diameter and height
        input diameter: The diameter of the cylinder
        input height: The height of the cylinder
    """
    return math.pi * (diameter/2)**2 * height



# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))

    # add test calls for your functions below
    # Tests for function 1
    print("cube(2) returns", cube(2))
    print("cube(-5) returns", cube(-5))

    # Tests for function 2
    print("slope(2, 3, 4, 7) returns", slope(2, 3, 4, 7))
    print("slope(7, 2, 3, 4) returns", slope(7, 2, 3, 4))
    print("slope(2, 3, 5, 3) returns", slope(2, 3, 5, 3))

    # Tests for function 3
    print("cylinder_volume(10, 10) returns", cylinder_volume(10, 10))
    print("cylinder_volume(20, 10) returns", cylinder_volume(20, 10))


