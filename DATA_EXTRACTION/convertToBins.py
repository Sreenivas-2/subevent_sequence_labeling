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

def SplitIntoBins(df):
	'''
		Splits the data into bins according to our input format
	'''

	input_ = []
	prev =  ''

	index = 0
	while index < df.shape[0]:
		dict_ = {}

		start_index = index
		row = df.iloc[index]
		time = row['tweet_time']
		dict_[row['label']] = 1

		list__ = []
		list_ = []
		list_.append(row['tweet_time'])
		list_.append(row['tweet_text'])
		list__.append(list_)

		index += 1
		while index < df.shape[0] and df.loc[index]['tweet_time'] - time <= 60:
			row = df.loc[index]
			list_ = []
			list_.append(row['tweet_time'])
			list_.append(row['tweet_text'])
			list__.append(list_)
			index += 1

			if row['label'] in dict_:
				dict_[row['label']] += 1
			else:
				dict_[row['label']] = 1

		label =  max(dict_.items(), key = operator.itemgetter(1))[0]
		str_ = "{'corrected_tags': '"
		if prev == 'B-' + label or prev == 'I-' + label:
			prev = 'I-' + label
			str_ += 'I-' + label
		else:
			prev = 'B-' + label
			str_ += 'B-' + label

		str_ += "'," + " 'event_type': '" + label + "', 'event_id': " + str(labels[label]) + ", 'doc': '" + row['event'] + "'}"

		list_ = []
		list_.append(str_)
		input_.append(list_)

		for line in list__:
			input_.append(line)

	# print(input_)
	return input_




def main(df):

	# Converting all the timestamps into unix
	for index, row in df.iterrows():
		row['tweet_time'] = convertToUnix(str(row['tweet_time']))

	# Sort the tweets by timestamps
	df = sortTweets(df)

	# Split the data into bins
	L = SplitIntoBins(df)

	with open('data.csv', 'w', newline = "") as f:
		writer = csv.writer(f, delimiter = '\t')
		writer.writerows(L)

if __name__ == '__main__':

	arg = sys.argv[1:]

	df = pd.read_csv(arg[1], encoding = 'utf-8')

	df =  df[['tweet_time', 'tweet_text', 'event', 'label']]

	# Creating dictionary for labels
	labels = {}
	if arg[0] == '--train':
		labels_ = set(list(df['label']))
		for ind, ele in enumerate(labels_):
			labels[ele] = ind

	main(df)










