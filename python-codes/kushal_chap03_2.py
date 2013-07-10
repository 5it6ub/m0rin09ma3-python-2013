#!/usr/bin/env python2
''' testhundred.py '''
number = int(raw_input("Enter an integer: "))
if number < 100:
    print "Your number is smaller than 100"
else:
    print "Your number is greater than equal to 100"

''' investment.py '''
amount = float(raw_input("Enter amount: "))
intrate = float(raw_input("Enter interest rate: "))
period = int(raw_input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (intrate*amount)
    print "Year %d Rs. %.2f" % (year, value)
    amount = value
    year += 1
