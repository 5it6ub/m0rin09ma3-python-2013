#!/usr/bin/env python

#tweetup -f path/to/image -d description
from twython import Twython
from optparse import OptionParser
import argparse

parser = OptionParser()
parser.add_option("-f", "--file", dest="img_file",
                  "-d", "--description", dest="description",
                  help="file: jpg, png, etc", metavar=FILE)
(option, args) = parser.parse_args()

print "file: %s\ndescription: %s" % (option.img_file, option.description)
APP_KEY = 'Z67CQZqw1KvstCCMXGkQ'
APP_SECRET = 'NaxaXxCoCAkZRf0mW4K36Je0WJuc4v5RYWfCu5es5I'
OAUTH_TOKEN = '1626564704-njhaT0EMeqEB8cYP4B3EuVAjmgMY9Fgx6zY5saq'
OAUTH_TOKEN_SECRET = 'f11zLz17j0yJUIuvoOOAMlJhuqeOQbDMe5dorx8AtWg'

#twitter = Twython(APP_KEY, APP_SECRET)
#auth = twitter.get_authentication_tokens()
#print auth
#OAUTH_TOKEN = auth['oauth_token']
#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# User Information
#credentials = twitter.verify_credentials()
#print credentials

# Authenticated Users Home Timeline
#home_timeline = twitter.get_home_timeline()
#print home_timeline

# Updating Status
# please make sure you set 'Access level' to permit POST
#post_status = twitter.update_status(status='See how easy using Twython is!')
#print post_status

# Searching
#search_result = twitter.search(q='python', result_type='popular')
#print search_result

# Updating Status with Image
photo = open('/home/skaetsu/downloads/python-logo-master-v3-TM.jpg', 'rb')
img_post_status = twitter.update_status_with_media(status='Checkout this cool image!', media=photo)
print img_post_status

