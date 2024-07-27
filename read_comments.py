import os
from dotenv import load_dotenv
from praw import Reddit


# Reddit user object
load_dotenv()
reddit = Reddit(
	client_id=str(os.getenv("CLIENT_ID")),
	client_secret=str(os.getenv("CLIENT_SECRET")),
	user_agent="reddit_reader by user")

URL = str(os.getenv("TARGET_URL"))

post = reddit.submission(url = URL)




