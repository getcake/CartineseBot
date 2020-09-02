import random
import config
import praw
import time
import random as rd
import cart


def authenticate():
    reddit = praw.Reddit(username=config.username,
                         password=config.password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent=config.user_agent)
    return reddit


def run(reddit):

    for comment in reddit.subreddit('testingground4bots').stream.comments(skip_existing=True):
        if "!cartibot" in comment.body and comment.id and not comment.saved:
            try:

                #msg = "\n\nThis is a test. I am a bot."
                print("Called")
                parent = comment.parent()
                parBod = parent.body
                with open('test.txt', 'r') as cstr:

                    cart.translate(parBod)
                    cartStr = cstr.read()
                    comment.save()
                    comment.reply(cartStr)  # TODO REPLY CONTENTS OF FILE !!
                    print("Replied")

            except Exception as e:
                print(e)
                time.sleep(30)

    time.sleep(60)