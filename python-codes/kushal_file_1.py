#!/usr/bin/env python2
''' showfile.py '''
name = raw_input("Enter the file name: ")
f = open(name)
print f.read()
f.close()
