import json
import tweepy
import pandas as pd
# import matplotlib.pyplot as plt

consumer_key = 'p6IMC2NbVsfepNKLxNiW0MzyU'
consumer_secret = 'UgMLRJ8VCG7RtgKSjdCIQ4RGTkbQHNvj4rMS8xg1CCc12i7CPN'

access_token = '91634289-6YbAoroDNn1mqkkq1lJnGyVfG2DWIFm0l1xRsmFby'
access_token_secret = 'vnwKLn7vd93BmhUiBQ41Y5aNRbhFUOXtzSbnmXzIpxVFS'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=OAUTH_TOKEN,
                  access_token_secret=OAUTH_TOKEN_SECRET
)

q = '#NoDAPL' #hashtags
count = 100 #no. of tweets