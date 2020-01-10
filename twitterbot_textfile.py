import tweepy
import redis
import sys

from time import sleep
from credentials import *

#from os import environ
#consumer_key = environ['CONSUMER_KEY']
#consumer_secret = environ['CONSUMER_SECRET']
#access_key = environ['ACCESS_KEY']
#access_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

key = 'line'
r = redis.from_url(os.environ.get("REDIS_URL"))
line_index = r.get(key)
if not line:
    line = 0

# Open text file endlessdisco.txt for reading
my_file = open('endlessdisco.txt', 'r')

# Read lines one by one from endlessdisco.txt and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Check if there are still lines to write
if line_index + 1 > len(file_lines):
    sys.exit("Not enought lines")

# Get the right line to send
line = file_lines[line_index]

# Try to send the line to Twitter
try:
    print(line)
    if line != '\n':
        api.update_status(line)
        r.set(key, line_index + 1) # Write the index to the DB
    else:
        pass
except tweepy.TweepError as e:
    print(e.reason)
