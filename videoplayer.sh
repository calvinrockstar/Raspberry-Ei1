#!/bin/sh

# get rid of the cursor so we don't see it when videos are running
setterm -cursor off

# set here the path to the directory containing your videos
VIDEOPATH="/home/pi/Desktop/Sensor" 

# you can normally leave this alone
SERVICE="omxplayer"

# now for our infinite loop!
while true; do
        if ps ax | grep -v grep | grep $SERVICE > /dev/null
        then
        sleep 1;
else
        for entry in $VIDEOPATH/*
        do
                #clear
                omxplayer $entry > /dev/null
		subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer1.sh", shell=True)
        done
	
fi
done