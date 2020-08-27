#! python3
#! Tweet Automatically

import config
import tweepy
import requests
import json

SEPT11DEATHS = 2977

# COVID Info Data
url = "https://api.covidtracking.com/v1/us/daily.json"

# Get Data from API
r = requests.get(url)
json_data = json.loads(r.text)

print(json_data[1])


# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

# Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#  Prints the latest tweets from your Timeline
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}\n")

# Tweet from Account!
# api.update_status("Test tweet from Tweepy Python")

covidDeaths = json_data[0]['death']

api.update_status(f'Quick Reminder! Today\'s US Covid Death Total: {covidDeaths}\n'
                  f'That\'s like {covidDeaths / SEPT11DEATHS} 9/11\'s !\n'
                  f'\n'
                  f'\n'
                  f'\n'
                  f'\n Great Job America!')

