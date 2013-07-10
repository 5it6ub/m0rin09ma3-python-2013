#!/usr/bin/env python2
''' continue.py '''
while 1:
    n = int(raw_input("Please enter an integer: "))
    if n < 0:
        continue # this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print "Squre is ", n ** 2
print "Goodbye"
