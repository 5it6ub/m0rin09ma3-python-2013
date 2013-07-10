#!/usr/bin/env python2
import math

def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side 
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print longest_side(4, 5)
