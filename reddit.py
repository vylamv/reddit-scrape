#! python3
import time
import praw
import pandas as pd 
import datetime as dt 
from config import client

items = ["metaverse", "shoko", "e6.5", "mizu"]

scanned = []

# Getting Reddit and subreddit instances
reddit = praw.Reddit(client_id='njDwlx3OS4B3Rg', \
                     client_secret='xmpXiyJGpzEcjkjdJVaKcBOrUYM', \
                     user_agent='scrape', \
                     username='xxxx', \
                     password='xxxx')


subreddit = reddit.subreddit('mechmarket')
# top_subreddit = subreddit.new()
top_subreddit = subreddit.new(limit=50)

def checkReddit():
    for submission in subreddit.new(limit=50):
        for i in items:
            if i in submission.title.lower() and submission.id not in scanned:
                print(submission.title, submission.id)
                scanned.append(submission.id)
                client.messages.create(to="+xxxx",
                            from_="+12029724875",
                            body=submission.title)
    time.sleep(30)

while True:
    checkReddit()

topics_dict = { "title":[], 
                "score":[], 
                "id":[], 
                "url":[],
                "comms_num": [],
                "created": [],
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
