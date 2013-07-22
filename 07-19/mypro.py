#!/usr/bin/env python
import sys

num = int(sys.argv[1])
for n in range(1,num+1):
    if n % 15:
        if n % 5:
            if n % 3:
                print '%d,' % n,
            else:
                print 'dgp,',
        else:
            print 'lug,',
    else:
        print 'dgp lug,',

