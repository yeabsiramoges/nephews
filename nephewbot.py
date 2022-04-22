import praw
import os

reddit = praw.Reddit(
    user_agent= 'android:nephews:0.1 by u/kingyeab',
    client_id=os.environ.get('REDDIT_PERSONAL_USE'),
    client_secret=os.environ.get('REDDIT_SECRET'),
    username="kingyeab",
    password=os.environ.get('PASS')
)