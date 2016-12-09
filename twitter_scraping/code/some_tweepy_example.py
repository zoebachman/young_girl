# got stuck somewhere halfway going through a tutorial

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



# tweets_data_path = '../data/twitter_data.txt'
tweets_data_path = 'searchResults_teen.json'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
# user = api.get_user('lilmiquela')
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

search = api.search("q=%23teen")

print search