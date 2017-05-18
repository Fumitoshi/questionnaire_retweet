import twitter
from datetime import datetime,timedelta
import time
api = twitter.Api(  consumer_key="",\
                    consumer_secret="",\
                    access_token_key="",\
                    access_token_secret="")

def lambda_handler(event,context):
    timeline = api.GetUserTimeline(count=200)

    yesterday = datetime.today() - timedelta(days=1)

    for tweet in timeline:
        created_at = datetime.strptime(tweet.created_at,"%a %b %d %H:%M:%S +0000 %Y")
        if created_at > yesterday:
            if tweet.text.find('アンケート') > -1:
                if tweet.retweeted == True:
                    status = api.GetStatus(tweet.id,include_my_retweet=True)
                    if status.current_user_retweet:
                        api.DestroyStatus(status.current_user_retweet)
                        api.PostRetweet(tweet.id)
                else:
                    api.PostRetweet(tweet.id)
