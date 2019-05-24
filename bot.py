import os
import tweepy
import requests

# all the keys the twitter requires
consumerKey = os.environ['BIGFOOT_CLASSINATOR_TWITTER_CONSUMER_KEY']
consumerSecret = os.environ['BIGFOOT_CLASSINATOR_TWITTER_CONSUMER_SECRET']
accessKey = os.environ['BIGFOOT_CLASSINATOR_TWITTER_ACCESS_KEY']
accessSecret = os.environ['BIGFOOT_CLASSINATOR_TWITTER_ACCESS_SECRET']

# where we go for classination
CLASSINATION_URL = 'http://bigfoot-classinator.herokuapp.com/classinate'

# human readable tweet bodies
MESSAGES = {
  'Class A': "You saw bigfoot! That's a Class A sighting.",
  'Class B': "You found some evidence of bigfoot like a footprint! That's a Class B sighting.",
  'Class C': "Someone told you about seeing bigfoot! That's a Class C sighting"
}

# this class receives tweets as they arrive
class BigfootClassinatorStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):

      # get the data from the tweet
      id = tweet.id_str
      text = tweet.text
      coords = tweet.coordinates

      # remove the hashtag from the string
      sighting = text.lower().replace("#bigfootclassinator", "")

      # get the coordinates
      longitude, latitude = -82.340507, 39.332019
      if coords is not None:
        longitude, latitude = coords['coordinates']

      # process the request
      request_json = { 'latitude': latitude, 'longitude': longitude, 'sighting': sighting }
      response_json = requests.post(CLASSINATION_URL, json=request_json).json()

      # get a good message
      classination = response_json['classination']['selected']
      message = MESSAGES[classination]

      # announce the classination to the world
      api.update_status(message, in_reply_to_status_id=id, auto_populate_reply_metadata=True)

      # log it all
      print(id, text, coords, longitude, latitude, classination)


# authenticate
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

# start listening for tweets with the correct hashtag
streamListener = BigfootClassinatorStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=['#BigfootClassinator'])
