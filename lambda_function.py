import twitter

api = twitter.Api(  consumer_key="",\
                    consumer_secret="",\
                    access_token_key="",\
                    access_token_secret="")

def lambda_handler(event,context):
    timeline = api.GetUserTimeline(count=200)

    for tweet in timeline:
        if tweet.text.find('アンケート') > -1:
            if tweet.retweeted == True:
                status = api.GetStatus(tweet.id,include_my_retweet=True)
                if status.current_user_retweet:
                    api.DestroyStatus(status.current_user_retweet)
                    api.PostRetweet(tweet.id)
            else:
                api.PostRetweet(tweet.id)
