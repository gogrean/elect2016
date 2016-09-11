import os
import sys
import time
import datetime
import sqlite3

import tweepy
import pandas as pd
import numpy as np
import yaml

root_dir = "../"
twitter_cred = yaml.load(open(root_dir + 'credentials/twitter.cred'))

auth = tweepy.OAuthHandler(twitter_cred['consumer_token'], 
                           twitter_cred['consumer_secret'])
auth.set_access_token(twitter_cred['access_token_key'], 
                      twitter_cred['access_token_secret'])

api = tweepy.API(auth)

con = sqlite3.connect("../data/trumps_followers.db")

con.execute("""CREATE TABLE IF NOT EXISTS trumpsFollowers(id INTEGER PRIMARY KEY, screen_name, 
                                                          created_at, name, lang, friends_count, 
                                                          followers_count, statuses_count, favorites_count, 
                                                          profile_image_url, verified)""")

def get_list(follower):
    created_at = datetime.datetime.strptime(follower._json['created_at'], 
                                            '%a %b %d %H:%M:%S %z %Y')
    created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S')
    return (follower._json['id'], follower._json['screen_name'], 
            created_at_str, follower._json['name'],
            follower._json['lang'], follower._json['friends_count'], 
            follower._json['followers_count'], follower._json['statuses_count'], 
            follower._json['favourites_count'], 
            follower._json['profile_image_url'], follower._json['verified'])

# https://dev.twitter.com/rest/reference/get/followers/list
# At this time, results are ordered with the most recent following first — however, 
# this ordering is subject to unannounced change and eventual consistency issues.
users = tweepy.Cursor(api.followers, screen_name="realDonaldTrump").items()

users_list = []
# http://stackoverflow.com/questions/31000178/how-to-get-large-list-of-followers-tweepy
while True:
    try:
        follower = next(users)
        users_list.append(get_list(follower))
    except (tweepy.RateLimitError):
        con.executemany("""INSERT OR REPLACE INTO trumpsFollowers(id, screen_name, 
                                                                  created_at, name, lang, 
                                                                  friends_count, followers_count, 
                                                                  statuses_count, favorites_count, 
                                                                  profile_image_url, verified) 
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", users_list)
        # Save changes to the database.
        con.commit()
        print("Writing new users and then waiting 15 minutes before getting more users.")
        time.sleep(900)
        users_list = []
        follower = next(users)
        users_list.append(get_list(follower))
    except StopIteration:
        con.close()
        break


