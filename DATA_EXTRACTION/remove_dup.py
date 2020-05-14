'''
	Removes duplicate tweets
'''

import pandas as pd

df = pd.read_csv('test.csv')
df = df.drop_duplicates(subset = 'tweet', keep = 'first')
df.to_csv('final1.csv', index = False)