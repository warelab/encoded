# !bin/bash
#fetch the indexing time for each 0.1 of a second until status of waiting then
# calc start and end time. 
counter=0
SECONDS=0
	startTime=$(date 2>&1)
echo "StartTime: " $startTime
	indexerOutput=$(python jsonParse.py 2>&1)
while [ "$indexerOutput" == "indexing" ]
	do
		elapsedTime=$SECONDS
		indexerOutput=$(python jsonParse.py 2>&1) 
		sleep 1
		((counter++))
	done
if [ "$indexerOutput" == "waiting" ];then
	
	endTime=$(date 2>&1)
	echo "EndTime: " $endTime
	
	echo "Elapsed time: " $elapsedTime 
fi
	  

export IT_FINISH=1
