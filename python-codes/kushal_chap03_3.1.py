#!/usr/bin/env python2
N = 10
sum = 0
count = 0
while count < N:
    number = float(raw_input(""))
    sum += number
    count += 1
average = float(sum)/N

print "N = %d, Sum = %f" % (N, sum)
print "Average = %f" % average
