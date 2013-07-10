#!/usr/bin/env python2
fahrenhite = 0.0
print "Fahrenhite Celsius"
while fahrenhite <= 250:
    celsius = (fahrenhite - 32.0)/1.8 # Here we calculate the fahrenhite value
    print "%5.1f %7.2f" % (fahrenhite, celsius)
    fahrenhite += 25
