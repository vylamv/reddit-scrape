#! python3
import praw
import pandas as pd 
import datetime as dt 

# pip install twilio>=6.0.0
# pip install praw
# pip install pandas

# # get config from ignored file
from config import client 
from config import reddit

# pip install twilio>=6.0.0
# pip install praw
# pip install pandas


subreddit = reddit.subreddit('mechmarket')
keeb_subreddit = subreddit.new(limit=20)

for submission in subreddit.new(limit=1):
    print(submission.title, submission.id)

topics_dict = { "title":[], 
                "score":[], 
                "id":[], 
                "url":[],
                "comms_num": [],
                "created": [],
                "body":[]}

for submission in keeb_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)





# send SMS text messages
# client.messages.create(to="+xxxxxxxxx",
#                         from_="+xxxxxxxxxxx",
#                         body="this is a test message")





""" config.py file 
import praw 
from twilio.rest import Client 

client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD') 
"""
