import tweepy
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

# Open text file endlessdisco.txt for reading
my_file = open('endlessdisco.txt', 'r')

# Read lines one by one from endlessdisco.txt and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(7200)
