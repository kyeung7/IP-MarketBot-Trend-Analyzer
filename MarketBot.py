# Kevin Yeung
# I parses select key (words and phrases)
# from comments/tweets to learn and predict market trends.

#test good and bad words list for AI
goodWords = []
badWords = []

#need to install tweepy via pip as well
import os
import tweepy as tw # twitter api package, need developer access on account
import pandas as pd

import analyze as analyze
import score as score

# authentication, access token to be revoked each repository push
consumer_key= 'L3Jwc5ku0gIkhYoGKyGIafTHc'
consumer_secret= 'G6wDAaufSzPrjMU3LPSm4e8l55BvVnRnK1Fh0Xk2c92DnMPy1u'
access_token= 'REDACTED'
access_token_secret='REDACTED'

def runBot():
    print('MarketBot is running ...')

    updateSearchTerms()
    
    # login, may need to refresh api token
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # example string for trend 'market crash
    search_words = "#market -filter:retweets" #"#cliametsfs+change -filter:retweets"
    date_since = "2020-5-30"

    tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(1000)

    fullStr = ''
    # tweets object contains the 5 most recent and revelant tweets
    for tweet in tweets:
        print(tweet.text)
        fullStr += format(tweet.text)
    ####print(fullStr)
    score.interpret(goodWords, badWords, fullStr)
    
def format(word): #creates long strings
    tempStr = ''
    for t in word:
        if t.isalpha():
            tempStr += t.lower()

    #print(tempStr)
    #interpret(tempStr)
    return tempStr   

# Updates words list using defintions csv
def updateSearchTerms():
    goodWords, badWords = analyze.getWords()
    print(goodWords)
    print(badWords)


runBot()
