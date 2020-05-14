'''
	Converts json to csv
'''

import json
import csv
import sys

arg = sys.argv[1]

input_ = []

list_ = []
list_.append('tweet_id')
list_.append('tweet_time')
list_.append('tweet_text')
list_.append('event')
input_.append(list_)

with open('output.txt') as f:
	for line in f:
		data = json.loads(line)

		list_ = []
		list_.append(data['id'])
		list_.append(data['created_at'])
		list_.append(data['text'])
		list_.append(arg)
		input_.append(list_)

with open('data.csv', 'w', newline = "") as f:
	writer = csv.writer(f)
	writer.writerows(input_)
