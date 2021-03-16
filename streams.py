import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    self.me = api.me()

  def on_status(self, tweet):
    print(f"{tweet.user.name}:{tweet.text}")

  def on_error(self, status):
    print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZFbsPeShZrxTDCdkNSXg1LLPR", 
  "66oYJHM70Sf2Zh3eRZeRMNesnApbIwjbci0IIdsxWdwommToFM")
auth.set_access_token("2786904242-jNGhsITOkfTNbaghYREM9obiq3OBYwB5WWwmOqc", 
  "mTQZwY5OohwcY5Uj9QOuS7E6hBKO4Zafl7I6f18HmcO2X")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])

tweets = api.mentions_timeline()
for tweet in tweets:
  tweet.favorite()
  tweet.user.follow()

for tweet in tweepy.Cursor(api.home_timeline).items(100):
  print(f"{tweet.user.name} said: {tweet.text}")