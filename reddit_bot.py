import praw
import config
import time

def bot_login():
    return praw.Reddit(username = config.username,
                       password = config.password,
                       client_id = config.client_id,
                       client_secret = config.client_secret,
                       user_agent = "numba1hydrohomie's Hydro Homie")

def run_bot(r):
    comment_ids = set()

    while True:
        for comment in r.subreddit("HydroHomies").comments(limit=25):
            if config.username == comment.author.name:
                continue
            if comment.id in comment_ids:
                continue

            if "water" in comment.body:
                print(f"Thirst Quenched For {comment.author.name}")
                comment.reply("I too love water")
                time.sleep(2)

            comment_ids.add(comment.id)

        time.sleep(300)

if __name__ == "__main__":
    r = bot_login()
    run_bot(r)
