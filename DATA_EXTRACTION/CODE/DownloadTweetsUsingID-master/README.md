(1) For extracting tweeets from tweetids :

	# DownloadTweetsUsingID
	This jar file for dowloading Json Tweets based on their ID.

	----
	## Requirements
	- You need tokens from Twitter like:
	  - consumer.key
	  - consumer.secret
	  - access.token
	  - access.token.secret
	- Put them into   `twitter.properties`

	----
	## Running
	- Step1: Create the file of IDs tweets under text [sample](https://github.com/quanap5/DownloadTweetsUsingID/blob/master/sample_tweet_ids_Nepal.txt)

	- Step2: Configuration as Requirement

	- Step3: Run JAR file with following command
	`java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool sample_tweet_ids_Nepal.txt out.txt`

	Note: To run again delete previous out.txt or rename output file.

(2) sort_tweets.py : This file sorts the csv file on timestamp

(3) jsonTocsv.py : This file converts the json file (output.txt) into csv file (sort_tweets operation takes place in this).

