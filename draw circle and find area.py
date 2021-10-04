from __future__ import print_function, division

import math
import turtle


def polyline(t, n, length, angle):
    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc1(t, r, n, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r, n):

    arc1(t, r, n, 360)

def move(t, length):
    
    t.pu()
    t.fd(length)
    t.pd()

def areatri(r, n, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    b = arc_length / n
    c = b/2
    a = math.pow(r,2) - math.pow(c,2)
    h = math.sqrt(a)
    
    area = (1/2)*b*h

    return area

def areacirc(r, n, angle):

    area = n * areatri(r, n, angle)

    return area

def areadiff(x, n, r):

    perfcirc = math.pi * r * 2

    diff = x - perfcirc

    print("Difference of area of circle with", n, " polyline with a perfect circle =", diff)


if __name__ == '__main__':
    
    scr = turtle.Turtle()
    radius = 60
    
    move(scr,-300)
    circle(scr, radius, 62)

    move(scr,300)
    circle(scr, radius, 12)

    move(scr,300)
    circle(scr, radius, 6)
    
    print("Area of circle with 62 polylines =", areacirc(radius, 62, 360))
    print("Area of circle with 12 polylines =", areacirc(radius, 12, 360))
    print("Area of circle with 6 polylines =", areacirc(radius, 6, 360))
    
    areadiff(areacirc(radius, 62, 360), 62, radius)
    areadiff(areacirc(radius, 12, 360), 12, radius)
    areadiff(areacirc(radius, 6, 360), 6, radius)
    
    turtle.mainloop()