import pandas as pd

df = pd.read_csv('../2015_nepal_eq_ids/tweet_ids/150425104337_nepal_earthquake_20150425_vol-1.json.csv')['tweet_id']
df.to_csv('input.txt', index = False)