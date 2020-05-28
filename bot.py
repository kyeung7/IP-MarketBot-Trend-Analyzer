# Kevin Yeung
# I parses select key (words and phrases)
# from comments/tweets to learn and predict market trends.

import os
import tweepy as tw # twitter api package, need developer access on account
import pandas as pd

# authentication, access token to be revoked each repository push
consumer_key= 'L3Jwc5ku0gIkhYoGKyGIafTHc'
consumer_secret= 'G6wDAaufSzPrjMU3LPSm4e8l55BvVnRnK1Fh0Xk2c92DnMPy1u'
access_token= '942395186222641153-8hsbFlVsvcWoTs6Hq96Wj7zczznGIRB'
access_token_secret= 'wMhhplcuiucp2pi2WOUiOdOU37dLBH4CsV8PsSwuKAmwZ'

def runBot():
    print('MarketBot is running ...')

    # login, may need to refresh api token
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # example string for trend 'market crash
    search_words = "#market crash"
    date_since = "2020-3-10"

    tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

    # tweets object contains the 5 most recent and revelant tweets
    for tweet in tweets:
        print(tweet.text)

runBot()
