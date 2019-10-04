# WhisperOuLoud

WhisperOutLoud is the twitter's closed account Best Friend! It's a twitter bot that is intended to help the hidden people of twitter(closed account used) contact the outside world (open account user world). The bot works like a proxy. You tag him in the tweet, and then he copy's your tweet in his account, in response to your own tweet.

## How to use it
Follow the bot, then wait it to follow you back. After that you need to use the tweet's in the following pattern.

`@bot_account #whisperoutloud The text body that will be written in the bot's tweet`

Then the bot will tweet all the text after the hashtag in his account in response to your tweet.


## Developing

The first think you need to do is to get a twitter bot credential aka developer account, and place in the respectives places in the credentials file.
[Look here(https://developer.twitter.com/en/application/use-case)
After that you need to install the requirements(tweepy)
```
pip install requirements.txt
```

After that you can simply run

```
python bot.py
```