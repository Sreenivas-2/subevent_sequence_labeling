import numpy as np
import csv
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

# nltk.download('punkt')
stop_words = set(stopwords.words('english'))

class pre_processing:

	# def __init__(self) :
		# return

	def deEmojify(self, text):
		return text.encode('ascii', 'ignore').decode('ascii')

	# Convert text to lowercase
	def to_lower(self, text) :
		return text.lower()

	def subj_lower(self, text) :
		return [ word.lower() for word in text]

	# Remove urls
	def remove_url(self, text) :
		return re.sub(r'(?i)\b((?:http?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', text)
	
	def remove_urls(self, text) :
		return re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', text)

	# Remove numbers
	def remove_numbers(self, text) :
		return re.sub(r'\d+', '', text)

	# Remove mentions
	def remove_s(self, text) :
		return re.sub(r'[#@][" "]*[^" "]+', '', text)
		# return re.sub(r"@.*[\t]", '', text)

	def is_match(text):
		print(text)
		# pattern = re.compile(r'@[^" "]+', text)
		return bool(re.search(r'@[^" "]+', text))

	#  Remove punctuation
	def remove_punctuation(self, text) :
		# table = str.maketrans(" "," ", string.punctuation)
		# return [str_.translate(table) for str_ in text]
		return text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))

	#  Remove whitespaces
	def remove_whitespaces(self, text) :
		return text.strip()

	#  Remove stopwords
	def remove_stopwords(self, text) : 
		tokens = word_tokenize(text)
		return [i for i in tokens if not i in stop_words]

	# Stemming 
	def stem_text(self, text) :
		stemmer = PorterStemmer()
		return [stemmer.stem(item) for item in text]

	# Extracting the nouns
	def pos_tagging(self, text) :
		text = word_tokenize(text)
		 # and not pos.startswith('NNP')
		return [token for token, pos in pos_tag(text) if pos.startswith('N') and pos != 'NNP']

	# Remove
	def remove_waste(self, text) :
		return [i for i in text if ".com" not in i and i != 'rt' and (len(i) != 1)]



# Remove duplicates from the data
df = pd.read_csv('input.csv')
df = df.drop_duplicates(subset = 'tweet_text', keep = 'first')


# Reading the tweet text
with open('output.csv', 'a') as fp:
	wr = csv.writer(fp, dialect = 'excel')
	list_ = []
	list_.append('tweet_id')
	list_.append('tweet_time')
	list_.append('tweet_text')
	list_.append('event')
	list_.append('label')
	wr.writerow(list_)

	# for i, line in enumerate(reader):
	for i, line in df.iterrows():
		print(i)
		tweet_text = line[2]
		if i != 0:

			# Creating Object
			obj = pre_processing()
			tweet_text = obj.deEmojify(tweet_text)
			tweet_text = obj.to_lower(tweet_text)
			tweet_text = obj.remove_urls(tweet_text)
			tweet_text = obj.remove_s(tweet_text)
			tweet_text = obj.remove_punctuation(tweet_text)
			tweet_text = obj.remove_whitespaces(tweet_text)
			tweet_text = obj.remove_stopwords(tweet_text)
			tweet_text = obj.remove_waste(tweet_text)

			if len(tweet_text) != 0:
				list_ = []
				list_.append(line[0])
				list_.append(line[1])
				list_.append(tweet_text)
				list_.append(line[-2])
				list_.append(line[-1])
				wr.writerow(list_)