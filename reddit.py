#! python3
import time
import praw
import pandas as pd
import datetime as dt
import config

items = ["metaverse", "shoko", "e6.5", "mizu", "key65"]

# Getting Reddit and subreddit instances
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.username,
                     password=config.password)


subreddit = reddit.subreddit('mechmarket')
top_subreddit = subreddit.new(limit=10)
scanned = set()


def checkReddit():
    for submission in subreddit.new(limit=10):
        for i in items:
            if i in submission.title.lower() and submission.id not in scanned:
                print(submission.title, submission.id)
                scanned.add(submission.id)
                config.client.messages.create(to=config.to,
                                              from_=config.from_,
                                              body=submission.title)
    time.sleep(30)


while True:
    checkReddit()

topics_dict = {"title": [],
               "score": [],
               "id": [],
               "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
