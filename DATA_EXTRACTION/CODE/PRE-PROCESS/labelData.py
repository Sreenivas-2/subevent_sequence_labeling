import pandas as pd

df = pd.read_csv('Otrain-dev1.csv')
# list_ = list(df['tweet_time'])
# print((df.loc[df['label'] == 'Other relevant information']).shape[0])
print(df['label'].value_counts(),df.shape[0])

# df.loc[df['label'] == 'Not related or irrelevant','label'] = 'O'
# df.loc[df['label'] == 'Not Relevant','label'] = 'O'
# df.loc[df['label'] == 'Sympathy and emotional support','label'] = 'prayers'
# df.loc[df['label'] == 'Missing, trapped, or found people','label'] = 'missing'
# df.loc[df['label'] == 'Infrastructure and utilities','label'] = 'infrastructure'
# df.loc[df['label'] == 'Shelter and supplies','label'] = 'shelter'
# df.loc[df['label'] == 'Volunteer or professional services','label'] = 'volunteer'
# # df.loc[df['label'] == 'Response Efforts','label'] = 'efforts'
# # df.loc[df['label'] == 'Response efforts','label'] = 'efforts'
# df.loc[df['label'] == 'Infrastructure Damage','label'] = 'infrastructure'
# df.loc[df['label'] == 'Infrastructure damage','label'] = 'infrastructure'
# df = df[(df.label == 'missing') | (df.label == 'infrastructure') | (df.label == 'volunteer') | (df.label == 'shelter')]
# df.to_csv('Otrain-dev1.csv')




# print(df.label.unique())
# print(df.shape[0])
# df.to_csv('Otrain-dev.csv', index = False)