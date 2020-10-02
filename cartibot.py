import random
import config
import praw
import time
import random as rd
import cart


def authenticate():
    reddit = praw.Reddit(
        username=config.username,
        password=config.password,
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent=config.user_agent,
    )
    return reddit


def run(reddit):

    for comment in reddit.subreddit(
        "traviscott+memes+teenagers+dankmemes+liluzivert+tylerthecreator+juicewrld+earlsweatshirt+hiphopcirclejerk+testingground4bots+playboicarti+hiphopheads"
    ).stream.comments(skip_existing=True):
        if (
            "!cartinesebot" in comment.body.lower()
            or "u/cartinesebot" in comment.body.lower()
            and comment.author != "cartinesebot"
            and not comment.saved
        ):
            try:

                msg = "*Beep Boop! I'm a bot! Please contact* [*u/cyanidesuppository*](https://reddit.com/user/cyanidesuppository) *with any issues or suggestions.* [*Github*](https://github.com/getcake/CartineseBot)"
                print("Called")
                parent = comment.parent()
                parBod = parent.body
                with open("test.txt", "r") as cstr:

                    if "!cartinesebot" not in parBod:

                        cart.translate(parBod)
                        cartStr = cstr.read()
                        comment.save()
                        comment.reply(
                            cartStr + "\n\n" + msg
                        )  # TODO REPLY CONTENTS OF FILE !!
                        print("Replied")

            except Exception as e:
                print(e)
                time.sleep(30)

    time.sleep(60)
