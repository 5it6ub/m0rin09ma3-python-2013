#!/usr/bin/env python2
''' quadraticequation.py '''
import math
a = int(raw_input("Enter value of a: "))
b = int(raw_input("Enter value of b: "))
c = int(raw_input("Enter value of c: "))
d = b*b - 4*a*c
root1, root2 = (0.0, 0.0)
if d < 0:
    print "ROOTS are imaginary"
else:
    root1 = (-b + math.sqrt(d)) / (2.0 * a)
    root2 = (-b - math.sqrt(d)) / (2.0 * a)
print "Root 1 = ", root1
print "Root 2 = ", root2
