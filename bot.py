#coding: utf-8

import tweepy
import time
import datetime

import credentials
import utils


class bot(object):
    def __init__(self):
        self.SLEEP_TIME = ((15 * 60) / 75) + 1
        self.hashtag = u"whisperoutloud"
        self.last_tweet = None
        self.last_own_tweet = None
        self.auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        self.auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def get_last_tweet_id(self):
        return self.last_tweet

    def answer_tweets(self):
        tweets = self.api.mentions_timeline(since_id=self.last_tweet)
        if len(tweets) > 0:
            self.last_tweet = tweets[-1].id
            print(self.last_tweet)

        for tweet in tweets:
            tweet = self.api.get_status(tweet.id, tweet_mode="extended")

            # Credentials for your Twitter bot account
            user = tweet.user
            hashtags = tweet.entities["hashtags"]
            text = utils.format_text(tweet.full_text, self.hashtag)
            name = user.screen_name
            in_reply_id = tweet.id

            if not utils.verify_tweet(user, hashtags, self.hashtag):
                return 0

            print("Helping {}!".format(name))
            status_text = utils.format_to_status_text(name, text)
            print("------------------------")
            print(status_text)
            print("------------------------")

            new_tweet = self.api.update_status(
                status=status_text,
                in_reply_to_status_id=in_reply_id,
                auto_populate_reply_metadata=True)
            self.last_own_tweet = new_tweet.id

    def run(self):
        now = datetime.datetime.now()
        dt_now = now.strftime("%d/%m/%Y %H:%M:%S")

        initial = self.api.update_status(status="Now running --- " + dt_now)

        self.last_tweet = initial.id
        followers_count = 0
        while True:
            followers_count = utils.update_followers(self.api, followers_count)
            self.answer_tweets()
            time.sleep(self.SLEEP_TIME)

if __name__ == "__main__":
    running_bot = bot()
    running_bot.run()
