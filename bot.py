#coding: utf-8

import tweepy, time

from credenciais import *
from utils import *

hashtag = u"whisperall"
last_tweet = None
last_own_tweet = None
def get_last_tweet_id():
     pass

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def answer_tweets():
    global last_tweet
    tweets = api.mentions_timeline(since_id=last_tweet)
    if (len(tweets)):
        last_tweet = tweets[-1].id
        print last_tweet
    for tweet in tweets:

        tweet = api.get_status(tweet.id,tweet_mode="extended")

        user = tweet.user
        hashtags = tweet.entities["hashtags"]
        text = format_text(tweet.full_text,hashtag)
        nome = user.screen_name
        in_reply_id = tweet.in_reply_to_status_id
        
        if (not verify_tweet(user,hashtags,hashtag)):
            return 0
    
        print "Helping {}!".format(nome)
        status_text = format_to_status_text(nome,text)
        print status_text
        
        new_tweet = api.update_status(status=status_text,in_reply_to_status_id=in_reply_id,
        auto_populate_reply_metadata=True)
        global last_own_tweet
        last_own_tweet = new_tweet.id




def main():
    global last_tweet
    initial = api.update_status(status="Now running --- version alpha(1.000) ")
    sleep_time = ((15*60)/75) + 1
    last_tweet = initial.id
    followers_count = 0
    while (1):
        followers_count = update_followers(api,followers_count)
        answer_tweets()
        time.sleep(sleep_time)

main()
