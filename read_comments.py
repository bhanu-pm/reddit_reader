import os
from dotenv import load_dotenv
import time
from datetime import datetime

from praw import Reddit
from praw.models import MoreComments


# Reddit user object
load_dotenv()
reddit = Reddit(
	client_id=str(os.getenv("CLIENT_ID")),
	client_secret=str(os.getenv("CLIENT_SECRET")),
	user_agent="reddit_reader by user")

URL = str(os.getenv("TARGET_URL"))

# function to extract time from a 2d array
def sorter(my_list):
	return my_list[0]


# Reading the target post and its comments
post = reddit.submission(url = URL)
top_level_comments_obj = post.comments

top_level_comments = []
for comment in top_level_comments_obj:
	top_level_comments.append([comment.created_utc, comment.body])

# Sorting top level comments in order of newest first
top_level_comments.sort(reverse=True, key=sorter)

for comment in top_level_comments:
	created_time_utc = datetime.utcfromtimestamp(comment[0] - 25200).strftime('%Y-%m-%d %H:%M:%S')
	print(created_time_utc)
	print(comment[1])
	print("-"*20 + "\n")

