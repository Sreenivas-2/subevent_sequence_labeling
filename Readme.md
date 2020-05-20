
# Sub-event detection from twitter streams as a sequence labeling problem


Implementation of our paper
[Sub-event detection from twitter streams as a sequence labeling problem](https://arxiv.org/pdf/1903.05396.pdf).

# Requirements
* Ubuntu 16.04
* Anaconda 5.2.0
* Numpy 1.16.1
* Gensim 3.6.0
* Pytorch 0.4.1
* PrettyTable 0.7.2

## Task
The goal is, given a main event (i.e., soccer match), to identify its core sub-events (e.g., goals, kick-off, yellow cards) from Twitter streams.

## Configuration
The model has several parameters that could be specified in the configuration files (see [config](https://github.com/bekou/subevent_sequence_labeling/tree/master/tagger_bin/configs)).

## Run the model
There are two directories (one for the word-level model and one the tweet-level model)
```
./run_<name_of_the_model>.sh
```

## Notes

Please cite our work when using this software.

Giannis Bekoulis, Johannes Deleu, Thomas Demeester, Chris Develder. Sub-event detection from twitter streams as a sequence labeling problem, In the Proceedings of the 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics, 2019

# Description :
(1) tweet_tager is our model

(2) DATA_EXTRACTION : this contains all the data and codes for extracting the data

 ## ROAD MAP :


 ------ DATA EXTRACTION :::

	----- DATA ::: 

			-----> The dataset used was Nepal Earthquake 2015.Tweets extracted were (both train and test) between April 25 and April 28 2015. [We have labels only for train data]

			----- INPUT FORMAT ::: input format of files(train.csv, test.csv, dev.csv) needed for our model.

				  	sample input (This has two bins) :

						{'corrected_tags': 'B-infrastructure', 'event_type': 'infrastructure', 'event_id': 0, 'doc': 'NepalEQ'}
						1430126766.0	['airlifts', 'disaster', 'relief', 'nepal', 'pictures']
						1430126779.0	['drone', 'video', 'offers', 'aerial', 'perspective', 'nepal', 'devastation']
						1430126793.0	['urgent', 'donate', 'ajws', 'emergency', 'relief', 'fund', 'survivors']
						1430126823.0	['air', 'india', 'reduces', 'fare', 'kathmandu', 'sector', 'operate', 'additional', 'flights']
						1430126838.0	['youre', 'seeking', 'information', 'forget', 'utilise', 'local']
						{'corrected_tags': 'B-shelter', 'event_type': 'shelter', 'event_id': 1, 'doc': 'NepalEQ'}
						1430126888.0	['mission', 'burnaby', 'firefighters', 'heading', 'nepal', 'help', 'rescue', 'relief', 'cknw']
						1430126891.0	['work', 'debt', 'relief', 'created', 'new', 'trust', 'fund', 'benefit']
						1430126894.0	['want', 'help', 'visit', 'list', 'relief', 'organizations', 'responding']
						1430126895.0	['devastating', 'pictures']


					Here,

						corrected_tags : tag obtained for the bin after applying BIO tagging

						event_type : sub-event of the bin

						event_id : numbering for the sub-events

						doc : event name (here our event is NepalEQ.

		

	----- EXTRACTION :::
	
			(1) We have used online tool ('../CODE/DownloadTweetsUsingID-master') to extract tweets from tweetids.
			
			(2) After extracting the csv files (from tweetids), they are pre-preocessed and built according to our requirements.


 ------ MODEL :::
	
	---> Inputs for our model (train.csv, test.csv, dev.csv) are present in '../tweet_tagger/inputs' folder.

	---> In '../tweet_tagger/predictions' folder we have our predictions for dev and test set in the final files ('predictions_test.csv', 'predictions_dev.csv')


 
  ****** Every folder has a Readme attached with it ********
			       
