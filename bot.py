# Kevin Yeung
# I parses select key (words and phrases)
# from comments/tweets to learn and predict market trends.

#test good and bad words list for AI
goodWords = ['great', 'positive', 'valuable', 'capital', 'bull', 'green', 'up', 'rise']
badWords = ['bad', 'negative', 'poor', 'bear', 'drop', 'red', 'fall', 'down']

#need to install tweepy via pip as well
import os
import tweepy as tw # twitter api package, need developer access on account
import pandas as pd

# authentication, access token to be revoked each repository push
consumer_key= 'L3Jwc5ku0gIkhYoGKyGIafTHc'
consumer_secret= 'G6wDAaufSzPrjMU3LPSm4e8l55BvVnRnK1Fh0Xk2c92DnMPy1u'
access_token= 'REDACTED'
access_token_secret= 'REDACTED'

def runBot():
    print('MarketBot is running ...')

    # login, may need to refresh api token
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # example string for trend 'market crash
    search_words = "#stock -filter:retweets" #"#cliametsfs+change -filter:retweets"
    date_since = "2020-5-01"

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
    interpret(fullStr)
    
def format(word): #creates long strings
    tempStr = ''
    for t in word:
        if t.isalpha():
            tempStr += t.lower()

    #print(tempStr)
    #interpret(tempStr)
    return tempStr

def interpret(string):
    marketScore = 0
    for word in goodWords:
        if word in string:
            marketScore += 0.1
    for word in badWords:
        if word in string:
            marketScore -= 0.1

    print('test trend score: ' + str(marketScore))
        

##import os
##import pandas as pd
####import matplotlib.pyplot as plt #need pip install
####import seaborn as sns #need pip install
####import itertools
####import collections
####
#####need pip uninstallold numpy, then pip install new numpy-MKL
##### need to install numpy-version depending on python version.. so if 3.7, get cp37
####import tweepy as tw
####import nltk
####from nltk.corpus import stopwords
####import re
####import networkx
####
####import warnings
####warnings.filterwarnings("ignore")
####
####sns.set(font_scale=1.5)
####sns.set_style("whitegrid")
##
##consumer_key= 'L3Jwc5ku0gIkhYoGKyGIafTHc'
##consumer_secret= 'G6wDAaufSzPrjMU3LPSm4e8l55BvVnRnK1Fh0Xk2c92DnMPy1u'
##access_token= '942395186222641153-IxUJRnSdwh3iJrpWDUjeeiKTMlSe8Ow'
##access_token_secret= '5Jlx74ccYQb7uZxKJEN3rrMRhXAZ6lRZiu8n78VTqhjPJ'

runBot()
