#coding: utf-8

import tweepy, time, datetime

from credentials import *
from utils import *

#CONSTANTS
SLEEP_TIME = ((15*60)/75) + 1
hashtag = u"whisperoutloud"
last_tweet = None
last_own_tweet = None


def get_last_tweet_id():
     pass


def answer_tweets():
    global last_tweet
    tweets = api.mentions_timeline(since_id=last_tweet)
    if (len(tweets)):
        last_tweet = tweets[-1].id
        print(last_tweet)
    for tweet in tweets:

        tweet = api.get_status(tweet.id,tweet_mode="extended")
# Credentials for your Twitter bot account

        user = tweet.user
        hashtags = tweet.entities["hashtags"]
        text = format_text(tweet.full_text,hashtag)
        nome = user.screen_name
        in_reply_id = tweet.id
        
        if (not verify_tweet(user,hashtags,hashtag)):
            return 0
    
        print "Helping {}!".format(nome)
        status_text = format_to_status_text(nome,text)
        print("------------------------")
        print status_text
        print("------------------------")

        
        new_tweet = api.update_status(status=status_text,in_reply_to_status_id=in_reply_id,
        auto_populate_reply_metadata=True)
        global last_own_tweet
        last_own_tweet = new_tweet.id




def run():
    global last_tweet
    now = datetime.datetime.now()
    dt_now = now.strftime("%d/%m/%Y %H:%M:%S")

    initial = api.update_status(status="Now running --- " + dt_now)
    
    last_tweet = initial.id
    followers_count = 0
    while (1):
        followers_count = update_followers(api,followers_count)
        answer_tweets()
        time.sleep(sleep_time)

if (__name__ == "__main__"):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    run()
