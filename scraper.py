import praw
import config
import time
from twilio.rest import Client

# pip install -r requirements.txt to import necessary packages

reddit = praw.Reddit(client_id=config.personalUseScript,
                     client_secret=config.secret,
                     user_agent="keyboard-scrape",
                     username=config.redditUser,
                     password=config.redditPass)
subreddit = reddit.subreddit('mechmarket')

idOfPosts = set()
idOfPostsList = list()

while True:
    for submission in subreddit.new(limit=8):
        if submission.link_flair_text in ["Buying", "Selling"]:
            title = submission.title.lower()
            if ("rama" in title or "u80" in title) and submission.id not in idOfPosts:
                idOfPosts.add(submission.id)
                idOfPostsList.append(submission.id)

                client = Client(config.twilioSID, config.twilioToken)
                client.messages.create(
                    to=config.cell, from_=config.twilioNum, body=submission.url)

    if len(idOfPostsList) > 20:
        # take out the first 10
        idOfPostsList = idOfPostsList[10:]
        idOfPosts = set(idOfPostsList)

    time.sleep(31)
    print(len(idOfPostsList), len(idOfPosts))
