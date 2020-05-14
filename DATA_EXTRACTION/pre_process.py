import numpy as np
import csv
import re
import string
import nltk
# from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

# stop_words = set(stopwords.words('english'))

class pre_processing:

	# def __init__(self) :
		# return

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
		return re.sub(r'@[" "]*[^" "]+', '', text)
		# return re.sub(r"@.*[\t]", '', text)

	def is_match(text):
		print(text)
		# pattern = re.compile(r'@[^" "]+', text)
		return bool(re.search(r'@[^" "]+', text))

	#  Remove punctuation
	def remove_punctuation(self, text) :
		return text.translate(str.maketrans("","", string.punctuation))

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
		return [i for i in text if ".com" not in i and len(i) != 1]



# Reading the tweet text
with open("final1.csv","r") as file, open('test.csv', 'a') as fp :
	reader = csv.reader(file, delimiter = ",")
	wr = csv.writer(fp, dialect = 'excel')
	for i, line in enumerate(reader):
		print(i)
		tweet_text = line[1]
		if i != 0:
			# Creating Object
			obj = pre_processing()
			if bool(re.search(r'@[^" "]+', tweet_text)):
				continue
			tweet_text = obj.to_lower(tweet_text)
			tweet_text = obj.remove_urls(tweet_text)
			tweet_text = obj.remove_numbers(tweet_text)
			tweet_text = obj.remove_punctuation(tweet_text)
			tweet_text = obj.remove_whitespaces(tweet_text)
			tweet_text = tweet_text.split()
			# tweet_text = obj.remove_stopwords(tweet_text)
			tweet_text = obj.remove_waste(tweet_text)
			list_ = []
			list_.append(line[0])
			list_.append(tweet_text)
			wr.writerow(list_)
			# tweet_text = obj.pos_tagging(tweet_text)