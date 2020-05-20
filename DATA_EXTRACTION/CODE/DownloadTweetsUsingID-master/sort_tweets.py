import pandas as pd
import sys
import datetime
import operator
import time
import csv


def convertToUnix(t):
	'''
		Converts the timestamp to unix
	'''

	# print('time', time)
	months = {'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}

	list_ = t.split()
	month = int(months[list_[1]])
	date = int(list_[2])
	time_ = list_[3].split(':')
	hr = int(time_[0])
	min_ = int(time_[1])
	sec = int(time_[2])
	yr = int(list_[-1])
	dt = datetime.datetime(yr, month, date, hr, min_, sec)
	return time.mktime(dt.timetuple())


def sortTweets(df):
	'''
		Sorts tweets by tweet_time
	'''

	df = df.sort_values('tweet_time')
	return df


def main(df):

	# Converting all the timestamps into unix
	for index, row in df.iterrows():
		df.at[index, 'tweet_time'] = convertToUnix(str(row['tweet_time']))

	# Sort the tweets by timestamps
	df = sortTweets(df)

	df.to_csv('output.csv', index = False)










