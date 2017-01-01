import tweepy
from tweepy.auth import OAuthHandler
from textblob import TextBlob
import csv

consumer_key = 'CONSUMER KEY GOES HERE'
consumer_secret = 'CONSUMER SECRET GOES HERE'
access_token = 'ACCESS TOKEN GOES HERE'
access_token_secret = 'ACCESS TOKEN SECRET GOES HERE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump') #Enter any term here


csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)


for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    csvWriter.writerow([tweet.text.encode('utf-8'), analysis.sentiment])
csvFile.close()