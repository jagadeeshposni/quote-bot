import twitter
import yaml
from brainyquote import pybrainyquote as brainyquote
import random
import time

topics = ['motivational','technology','life','positive','love','sex','success'] 
while True:
    try:
        random_topic = random.choice(topics)
        tweet_to_tweet = brainyquote.get_quotes(random_topic)
        api = twitter.Api(consumer_key='rHWJj3HbolrmUZA6u7nGOe3zn', access_token_key='114764177-lQYEYky4gIftTZ8yKHOvt7rSjk1jfJfFNb355NnS', consumer_secret='PyUm0WH9ydUHjgPUoUxrD1kuQwcmmgIAs4f4xxvqgbTXYrhOKl', access_token_secret='0p5ANPLywX9fnsYcFvvCzLeDJzEjveiSWsA9ev5Gy35x4')
        status = api.PostUpdate(tweet_to_tweet[0])
        print(status.text)
        time.sleep(5)
    except Exception as ex:
        print('error has occured')
