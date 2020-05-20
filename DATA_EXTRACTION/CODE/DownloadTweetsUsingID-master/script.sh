#!/bin/bash

# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool infrastructure_id_20150426.txt out_infrastructure_id_20150426.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool infrastructure_id_20150427.txt out_infrastructure_id_20150427.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool missing_id_20150425.txt out_missing_id_20150425.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool missing_id_20150426.txt out_missing_id_20150426.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool missing_id_20150427.txt out_missing_id_20150427.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool shelter_id_20150425.txt out_shelter_id_20150425.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool shelter_id_20150426.txt out_shelter_id_20150426.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool shelter_id_20150427.txt out_shelter_id_20150427.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool volunteer_id_20150425.txt out_volunteer_id_20150425.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool volunteer_id_20150426.txt out_volunteer_id_20150426.txt
# java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool volunteer_id_20150427.txt out_volunteer_id_20150427.txt


python3 jsonTocsv.py NepalEQ infrastructure infrastructure_id_20150426
python3 jsonTocsv.py NepalEQ infrastructure infrastructure_id_20150427
python3 jsonTocsv.py NepalEQ missing missing_id_20150425
python3 jsonTocsv.py NepalEQ missing missing_id_20150426
python3 jsonTocsv.py NepalEQ missing missing_id_20150427
python3 jsonTocsv.py NepalEQ shelter shelter_id_20150425
python3 jsonTocsv.py NepalEQ shelter shelter_id_20150426
python3 jsonTocsv.py NepalEQ shelter shelter_id_20150427
python3 jsonTocsv.py NepalEQ volunteer volunteer_id_20150425
python3 jsonTocsv.py NepalEQ volunteer volunteer_id_20150426
python3 jsonTocsv.py NepalEQ volunteer volunteer_id_20150427
