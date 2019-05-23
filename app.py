import os
import tweepy

consumerKey = os.environ['BIGFOOT_CLASSINATOR_TWITTER_CONSUMER_KEY']
consumerSecret = os.environ['BIGFOOT_CLASSINATOR_TWITTER_CONSUMER_SECRET']
accessKey = os.environ['BIGFOOT_CLASSINATOR_TWITTER_ACCESS_KEY']
accessSecret = os.environ['BIGFOOT_CLASSINATOR_TWITTER_ACCESS_SECRET']

class BigfootClassinatorStreamListener(tweepy.StreamListener):
    def on_status(self, status):
      print(status.text)
      api.update_status("This is a reply test.", in_reply_to_status_id=status.id_str, auto_populate_reply_metadata=True)

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)


streamListener = BigfootClassinatorStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=['#BigfootClassinator'])
