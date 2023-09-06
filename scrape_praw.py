import praw
import pandas as pd
from datetime import datetime
# Initialize the Reddit API client with your credentials
reddit = praw.Reddit(
    client_id='hyuNcnJitHVl5jj4xiSX0w',
    client_secret='q7W9Jt22xIktV-t-4k_F3JDavfIihw',
    user_agent='social_ai'
)

# Define the subreddit and keyword you want to search for
subreddit_name = 'depression'
keyword = 'sad'

# Create an empty list to store relevant posts
relevant_posts = []

# Search for posts containing the keyword in the specified subreddit


#Fetch comments from relevant posts
# relevant_comments = []
# for post in relevant_posts:
#     post.comments.replace_more(limit=10)  # Fetch all comments
#     for comment in post.comments.list():
#         relevant_comments.append(comment.body)
#         print(comment.author_fullname)
#         break
# Print relevant posts and comments
def get_search_results(keyword):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.search(keyword, limit=10000):  # You can adjust the limit as needed
        relevant_posts.append(submission)
    df = pd.DataFrame(columns=["created_utc","Author","Title","Text","Score","Num_comments"])
    print(f"Found {len(relevant_posts)} relevant posts:")
    for post in relevant_posts:
        print("in code")
        df.loc[len(df)] = list([datetime.fromtimestamp(post.created_utc),post.author,post.title,post.selftext,post.score,post.num_comments])
    file_name = 'post_{}_{}.csv'.format(keyword, datetime.now().strftime("%Y-%m-%d %H%M%S"))
    df.to_csv(file_name)

    print("CSV is generated!!!")
    return file_name

def get_user_posts(user_id):
    df = pd.DataFrame(columns = ["created_utc","Text"])
    user = reddit.redditor(user_id)
    submissions = user.submissions.new(limit=None)
    #self_texts = []
    for link in submissions:
        if (link.selftext is not None) and (link.selftext != "[removed]"):
            df.loc[len(df)] = list([datetime.fromtimestamp(link.created_utc), link.selftext])
    file_name = 'user_{}.csv'.format(datetime.now().strftime("%Y-%m-%d %H%M%S"))
    df.to_csv(file_name)
    return file_name


#get_user_posts("Horaciow14")