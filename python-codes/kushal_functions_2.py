#!/usr/bin/env python2
''' local.py '''
def change(x=7):
    a = 90
    print a,

    global b
    b = x
    print b

a = 9
print "Before the function call ", a
print "inside change function",
change()
print "After the function call ", a

b += 5
print "Before the function call ", b
print "inside change function",
change(2)
print "After the function call ", b
