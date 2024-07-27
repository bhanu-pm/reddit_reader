import os
from dotenv import load_dotenv
from praw import Reddit


# Reddit user object
load_dotenv()
reddit = Reddit(
	client_id=os.getenv("CLIENT_ID"),
	client_secret=os.getenv("CLIENT_SECRET"),
	user_agent="reddit_reader by user")

URL = "https://www.reddit.com/r/postmates/comments/1dsmnm3/monthly_existing_user_promo_code_thread/"
post = reddit.submission(url = URL)




