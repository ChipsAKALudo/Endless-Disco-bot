import tweepy
import redis
import sys
import os

from time import sleep
from credentials import *
from random import randint

#from os import environ
#consumer_key = environ['CONSUMER_KEY']
#consumer_secret = environ['CONSUMER_SECRET']
#access_key = environ['ACCESS_KEY']
#access_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

my_file = open('endlessdisco.txt', 'r')
file_lines = my_file.readlines()
line = file_lines[randint(0, len(file_lines) - 1)]
print(line)

try:
    api.update_status(line)
except tweepy.TweepError as e:
    print(e.reason)
