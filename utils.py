def format_to_status_text(screen_name, text):
    return u"@{} said:\n\n{}".format(screen_name, text)


def format_text(text,hashtag):
    print(text)
    size = len(hashtag)
    slice_index = text.find(hashtag)
    slice_index += size
    new_text = text[slice_index:]
    return new_text


def verify_tweet(user, hashtags, hashtag):
    """
    The user needs to be protected otherwise his tweet can be seen
    The user will eventualy follow me so i can follow him back
    The user will be followed by me otherwise the tweet wont be seen
    """
    result = True
    if (hashtag not in (map(lambda x: x["text"], hashtags))):
        result =  False
        print(1)
    if (result) :
        print("deu bom")
    else:
        print("deu ruim")
    return result


def verify_new_follower(old_follower_number, api):
    result = api.me().followers_count > old_follower_number
    if (result):
        print("new followers found!")
    return result


def update_followers(api, old_follower_number):
    if verify_new_follower(old_follower_number,api):
        for follower in api.followers():
          
            friendship  = api.show_friendship(source_screen_name=api.me().screen_name, target_screen_name=follower.screen_name)

            if not friendship[0].following and not friendship[0].following_requested:
                print("Now {} is my best friend".format(follower.screen_name))
                api.create_friendship(screen_name=follower.screen_name)
                
    return api.me().followers_count

