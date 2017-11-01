pids=`ps ax | grep phantomjs | grep -v "grep" | cut -d" " -f1`
if [ "$pids" != "" ]; then
	kill -9 $pids;
fi
