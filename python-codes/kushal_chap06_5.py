#!/usr/bin/env python2
''' desingn1.py '''
row = int(raw_input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    print x
    n -= 1

''' design2.py '''
n = int(raw_input("Enter the number of rows: "))
i = 1
while i <= n:
    print "*" * i
    i += 1

''' design3.py '''
row = int(raw_input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    y = " " * (row - n)
    print y + x
    n -= 1
