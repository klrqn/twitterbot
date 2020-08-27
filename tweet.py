#! python3
#! Tweet Automatically

import config
import tweepy
import requests
import json
import inflect


SEPT11DEATHS = 2977

# COVID Info Data
url = "https://api.covidtracking.com/v1/us/daily.json"

# Get Data from API
r = requests.get(url)
json_data = json.loads(r.text)

# print(json_data[1])

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# connect to Twitter API
api = tweepy.API(auth)

# test connection
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    print('\n')

# Today's Daily Covid Deaths Total
covidDeaths = json_data[0]['death']

# Tweet Covid Update
# api.update_status(f'Quick Reminder! Today\'s US Covid Death Total: {covidDeaths}\n'
#                   f'That\'s like {"{:.2f}".format(covidDeaths / SEPT11DEATHS)} 9/11\'s !\n'
#                   f'\n'
#                   f'\n'
#                   f'\n'
#                   f'\n Great Job America!')

print(f'Just a quick reminder:\n'
      f'Today\'s US Covid Death Total is {covidDeaths}\n'
      f'That\'s like {inflect.engine().number_to_words("{:.0f}".format(covidDeaths / SEPT11DEATHS))} 9/11s!\n'
      f'.\n.\n.\n'
      f'Great Job America!')

# "{:.2f}".format(a_float)