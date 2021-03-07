import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZFbsPeShZrxTDCdkNSXg1LLPR", 
    "66oYJHM70Sf2Zh3eRZeRMNesnApbIwjbci0IIdsxWdwommToFM")
auth.set_access_token("2786904242-jNGhsITOkfTNbaghYREM9obiq3OBYwB5WWwmOqc", 
    "mTQZwY5OohwcY5Uj9QOuS7E6hBKO4Zafl7I6f18HmcO2X")

api = tweepy.API(auth)

try:
  api.verify_credentials()
  print("Authentication OK")
except:
  print("Error during authentication")