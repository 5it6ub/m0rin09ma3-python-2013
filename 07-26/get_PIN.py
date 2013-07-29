#!/usr/bin/env python
import sys
import tweepy

CONSUMER_KEY = 'Z67CQZqw1KvstCCMXGkQ'
CONSUMER_SECRET = 'NaxaXxCoCAkZRf0mW4K36Je0WJuc4v5RYWfCu5es5I'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
ACCESS_KEY = auth.access_token.key
ACCESS_SECRET = auth.access_token.secret
#print "ACCESS_KEY = '%s'" % auth.access_token.key
#print "ACCESSS_SECRET = '%s'" % auth.access_token.secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])
