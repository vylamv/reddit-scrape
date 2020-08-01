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
idOfPostsList = [None] * 20
listIndex = 0


while True:
    for submission in subreddit.new(limit=8):
        if submission.link_flair_text in ["Buying", "Selling"]:
            title = submission.title.lower()
            if ("rama" in title or "u80" in title) and submission.id not in idOfPosts:

                if (idOfPostsList[listIndex % 20]):
                    idOfPosts.remove(idOfPostsList[listIndex % 20])

                idOfPostsList[listIndex % 20] = submission.id
                idOfPosts.add(submission.id)
                listIndex += 1

                client = Client(config.twilioSID, config.twilioToken)
                client.messages.create(
                    to=config.cell, from_=config.twilioNum, body=submission.url)

    time.sleep(31)
    # to prevent integer overflow
    if listIndex % 20 == 0:
        listIndex = 0
    print(len(idOfPostsList), len(idOfPosts))
