#!/usr/bin/env python2
''' integer.py '''
days = int(raw_input("Enter days: "))

#months = days / 30
#days = days % 30
#print "Months = %d Days = %d" % (months, days)
print "Months = %d Days = %d" % (divmod(days, 30))
