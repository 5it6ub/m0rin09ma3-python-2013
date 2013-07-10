#!/usr/bin/env python2
import os
import sys

def parse_file(path):
    """
    Parses the text file in the given path and returns space, tab details.

    :arg path: Path of the text file to parse

    :return: A tuple with count of spaces, tabs and lines.
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close() # Now close the open file

    return spaces, tabs, i + 1

def main(path):
    """
    Function which prints counts of spaces, tabs and lines in a file.

    :arg path: Path of the text file to parse
    :return: True if the file exits or False.
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print "Spaces %d. tabs %d. lines %d" % (spaces, tabs, lines)
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
