import twitter
import json
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


statuses = api.GetSearch(term=q, count=count)

# status = statuses[0] to get each individual status

# get users who are tweeting
tweet_users = [x.user.screen_name for x in statuses]
tweet_users[:20]

# get sevral tweets
num_iterations = 30

for i in range(num_iterations):
	max_id = search_results[-1].id
	statuses += api.GetSearch(term=q, count=count, max_id=max_id)

# get text of tweets
status_texts = [ status.text for status in statuses ]

print json.dumps(status_texts[0:5], indent=1)