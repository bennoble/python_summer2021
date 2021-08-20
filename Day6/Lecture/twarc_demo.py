# a script to pull down all tweets from a list of users 
# between two dats and write them to a csv
# for more, see https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/6a-labs-code-academic-python.md

# pip3 install twarc
from twarc import Twarc2, expansions
import json
import datetime
import os
import csv
import pandas as pd

# start up the client with your academic bearer token
client = Twarc2(bearer_token="")

# specify the filepath and name
filename = '/Users/bennoble/Desktop/test.csv'

## a list of links to cnadidate's twitter pages, this could also be read 
## directly from a csv of links using pandas
cand_twit = ['https://www.twitter.com/PerkinsForUSSen',
 'https://www.twitter.com/NewDayForNJ',
 'https://www.twitter.com/LaurenWitzkeDE',
 'https://www.twitter.com/schustercampai1',
 'https://www.twitter.com/cwesleymorgan']

with open(filename, 'w') as f: # open the csv writer
    writer = csv.DictWriter(f, fieldnames = ('twitter_handle', 'author_id', 'follower_count', 'created_at', 'tweet_id', 'text', 'rts', 'replys', 'likes', 'quotes', 'link', 'ref_tweet', 'ref_tweet_id', 'ref_tweet_user_id')) # define the columns
    writer.writeheader() # write the header
    tweet = {}
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2020, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2020, 11, 3, 0, 0, 0, 0, datetime.timezone.utc)

    for i in range(len(cand_twit)): # for each twitter profile
        print(i) # track progress
        user = cand_twit[i].split('/')[-1] # subset string to get the username
        query = "from:{}".format(user) # syntax for searching API for the user
        # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
        search_results = client.search_all(query=query, start_time=start_time, end_time=end_time)
        # Twarc returns all Tweets for the criteria set above, so we page through the results
        for page in search_results:
            # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
            # so we use expansions.flatten to get all the information in a single JSON
            result = expansions.flatten(page)
            for t in result: # for each individual tweet get the relevant info
                # author variables
                tweet['twitter_handle'] = t['author']['username'] # twitter username
                tweet['author_id'] = t['author']['id'] # internal twitter id
                tweet['follower_count'] = t['author']['public_metrics']['followers_count'] # num. followers today

                # tweet variables
                tweet['created_at'] = t['created_at'] # date of tweet
                tweet['tweet_id'] = t['id'] # internal tweet id
                tweet['text'] = t['text'] # text of tweet
                # tweet stats
                tweet['rts'] = t['public_metrics']['retweet_count']
                tweet['replys'] = t['public_metrics']['reply_count']
                tweet['likes'] = t['public_metrics']['like_count']
                tweet['quotes'] = t['public_metrics']['quote_count']
                # attachements
                try:
                    tweet['link'] = ts[0]['entities']['urls'][0]['display_url'] # try to get url of attachment if present
                except:
                    tweet['link'] = 'NA'
                try: 
                    tweet['ref_tweet'] = t['referenced_tweets'][0]['type'] # type of reference (e.g., RT, reply, etc)
                    tweet['ref_tweet_id'] = t['referenced_tweets'][0]['id'] # id of tweet being referenced
                    tweet['ref_tweet_user_id'] = t['in_reply_to_user_id'] #id of user being referenced
                except: 
                    tweet['ref_tweet'] = 'NA'
                    tweet['ref_tweet_id'] = 'NA'
                    tweet['ref_tweet_user_id'] = 'NA'
                writer.writerow(tweet) # write row to csv
