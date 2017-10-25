#!/usr/bin/env python3
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import json


consumer_key = "" # Add the consumer key
consumer_secret = "" # Add the consumer secret key
access_token = "" # Add the accsess token key
access_token_secret = "" # Add the accsess token secret key


class oauthHandler:
	"""  This class authenticates with the Twitter API   """
	def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_token_secret)
		self.getAPI()


	def getAPI(self):
		self.api = API(self.auth)
		print("DEBUG: " + self.api.me().name + " is no logged in and accsess API!")
		return self.api

	def getAuth(self):
		return self.auth


class pullTweet:
	"""  This class pull tweets with the Twitter API   """
	__metaclass__ = list
	def __init__(self):
		self.tweets = []
		self.pullTweets()

	def pullTweets(self):
		for self.tweet in Cursor(api.search, q="dftek",
								result_type='recent').items(10):
			if self.tweet:
				self.tweets.append(self.tweet._json)
		return self.tweets

class fileMeta(type):
	"""  This class supports FileOp class to create file object   """
	def __new__(cls, name, parents, dct):
		if 'class_id' not in dct:
			dct['class_id'] = name.lower()

		if 'file' in dct:
			filename = dct['file']
			dct['file'] = open(filename, 'w')

		return super(fileMeta, cls).__new__(cls, name, parents, dct)


class fileOp(object):
	"""  This class make the file operations  """
	__metaclass__ = fileMeta

	def __init__(self, jsonfile, tweets):
		for tweet in tweets:
			self.saveFile(tweet)

		self.closeFile()


	def saveFile(self, tweet):
		#print(dir(jsontweets))
		jsonfile.file.write(str(tweet))
		jsonfile.file.write('\n')

	def closeFile(self):
		jsonfile.file.close()



if __name__ == "__main__":
	con = oauthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
	auth = con.getAuth()
	api = API(auth)
	tweets = pullTweet()
	jsonfile = fileMeta('jsonfile', (), dict(file='devfest.json'))
	fileOp(jsonfile, tweets.tweets)