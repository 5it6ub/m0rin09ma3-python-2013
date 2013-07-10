#!/usr/bin/env python2
''' argvtest.py '''
import sys
print "First value", sys.argv[0]
print "All values"
for i, x in enumerate(sys.argv):
    print i, x
