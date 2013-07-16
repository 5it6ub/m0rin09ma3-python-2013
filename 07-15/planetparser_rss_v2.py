#!/usr/bin/env python
import sys
import feedparser
from optparse import OptionParser

def main():
    """
    Fetch RSS data from 'planet.fedoraobject.org/*.xml' and
    output blog-entry-title & blog-entry-author
    """

    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--type", dest="rss_type", default="RSS1",
                      help="set RSS1, RSS2, or ATOM", metavar="TYPE")
    (option, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")
    
    print 'RSS type is %s' % option.rss_type

    '''
    # fetch data
    rss_type = 'rss10.xml' # rss20.xml also has same format
    s_url = 'http://planet.fedoraproject.org/' + rss_type
    f = feedparser.parse(s_url)
    print 'Total number of post: %d' % len(f)

    for i in range(len(f)):
        print f.entries[i].title
    '''
    return 0

if __name__ == '__main__':
    sys.exit(main())
