import json
import tweepy
import pandas as pd
import matplotlib.pyplot as plt

consumer_key = 'p6IMC2NbVsfepNKLxNiW0MzyU'
consumer_secret = 'UgMLRJ8VCG7RtgKSjdCIQ4RGTkbQHNvj4rMS8xg1CCc12i7CPN'

access_token = '91634289-6YbAoroDNn1mqkkq1lJnGyVfG2DWIFm0l1xRsmFby'
access_token_secret = 'vnwKLn7vd93BmhUiBQ41Y5aNRbhFUOXtzSbnmXzIpxVFS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


user = api.get_user('slbedard ')
# user = api.get_user('sugaredlemon')

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name


# user_timeline = api.user_timeline('sugaredlemon', 10, 1)
# status = api.statuses_lookup('lilmiquela')

# print user_timeline
# for x in status:
# 	print x

# search = api.search("q=%23teen")

# print search