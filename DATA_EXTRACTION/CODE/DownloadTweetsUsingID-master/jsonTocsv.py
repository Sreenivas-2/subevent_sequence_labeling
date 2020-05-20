'''
	Converts json to csv
'''

import json
import csv
import sys
import sort_tweets as st

arg = sys.argv[1:]

input_ = []

list_ = []
list_.append('tweet_id')
list_.append('tweet_time')
list_.append('tweet_text')
list_.append('event')
list_.append('label')
input_.append(list_)

with open('output.txt') as f:
	for line in f:
		data = json.loads(line)

		list_ = []
		list_.append(data['id'])
		list_.append(data['created_at'])
		list_.append(data['text'])
		list_.append(arg[0])
		list_.append(arg[1])
		input_.append(list_)

df = pd.DataFrame(list_)
st.main(df)

