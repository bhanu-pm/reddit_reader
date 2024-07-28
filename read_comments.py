import os
from dotenv import load_dotenv
import time
from datetime import datetime
import json

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
def sorter(my_dict):
	return my_dict['time']


# Reading the target post and its comments
post = reddit.submission(url = URL)
top_level_comments_obj = post.comments

top_level_comments = []
for comment in top_level_comments_obj: # -25200 to change time zone to MST
	top_level_comments.append({'time':int(comment.created_utc)-25200, 'body':comment.body, 'replies':comment.replies})

# Sorting top level comments in order of newest first
top_level_comments.sort(reverse=True, key=sorter)

# Retrieving previously used comments to compare and find unseen latest comments
try:
	used_comments_obj = open('used_comments_file.json')
	used_comments_json = json.load(used_comments_obj)
	used_comments = used_comments_json['used_comments']
	used_comments_obj.close()
except:
	# print('Empty file')
	used_comments = None

# Inserting the latest comments in the to_be_used list, in order of oldest first
to_be_used = []

if used_comments is not None:
	for new_comment in top_level_comments:
		if new_comment['time'] > used_comments[0]['time']:
			to_be_used.insert(0, new_comment)
		else:
			break
elif used_comments is None:
	to_be_used.insert(0, new_comment)

# Sorted in the order of latest/newest first, joined at start to previously used comments
now_used = to_be_used.copy()
now_used.sort(reverse=True, key=sorter)
now_used.extend(used_comments)

used = {'used_comments': now_used}

with open('used_comments_file.json', 'w') as used_comments_file:
	json.dump(used, used_comments_file)
