# pylint: disable=no-member
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def petal(t,r,angle):
    """Draws a petal with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle
    """
    arc(t, r, angle)  
    t.lt(180-angle)   #lit the turtle project parrallel to the beginning 
    arc(t, r, angle)

def petals(t,r,angle,n):
    """Draws a flower with the given radius, angle and the number of petals.

    t: Turtle
    r: radius
    angle: angle
    n: number of petals
    """
    angle_rotate = float(360/n)
    for i in range(n):
        petal(t,r,angle)
        t.lt(180-angle+angle_rotate)


def flower1(t,r,angle,n):
    petals(t,r,angle,n)

def flower2(t,r,angle,n,overlap):
    """Draws a flower with the given radius, angle , the number of petals
    and the specific overlapping index.
    t: Turtle
    r: radius
    angle: angle
    n: number of petals
    overlap: index for overlapping
    """
    overlap = int(overlap)
    rotateangle = float(360/n)
    for i in range(overlap): 
        petals(t,r,angle,n)
        t.lt(-rotateangle/2)   #right rotate turtle object
    t.lt(rotateangle/2*overlap)
def example():
    """An example to show the effect of different radius and angle to a petal.
    """
    bob = turtle.Turtle()
    petal(t=bob,r=50,angle=60)
    bob = turtle.Turtle() #reset position and angle
    petal(t=bob,r=50,angle=180)
    bob = turtle.Turtle()
    petal(t=bob,r=100,angle=60)
    bob = turtle.Turtle()
    petal(t=bob,r=100,angle=180)
    bob = turtle.Turtle()
    petal(t=bob,r=150,angle=30)
    bob = turtle.Turtle()
    petal(t=bob,r=150,angle=180)


if __name__ == '__main__':
    bob = turtle.Turtle()
    #petal(bob,50,200)
    #flower1
    bob.pu()
    bob.fd(-150)
    bob.pd()
    flower1(bob,50,60,7)

    #flower2
    bob.pu()
    bob.fd(150)
    bob.pd()
    flower2(bob,60,60,5,2)

    #flower3
    bob.pu()
    bob.fd(150)
    bob.pd()
    flower1(bob,r=150,angle=20,n=20)
    # to avoid the overlapping between two near petals, arc with lager radius and small angle is required
    # following is a example to help understanding

    turtle.mainloop()