import subprocess
import time
import pexpect
import random
#import vidtest

from serial import Serial
from subprocess import PIPE, STDOUT
ser = Serial('/dev/ttyACM0', 115200, timeout=1)

def receiving(ser):
    global last_received
    global startVideo
    global isPlaying

    startVideo = 0
    buffer = ''
    isPlaying = 0
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        	
        if '\n' in buffer:
            lines = buffer.split('\n')
            last_received = lines[-2]
            buffer = lines[-1]
	    print(last_received)
	    selected = random.choice(['1', '2', '3','4','5','6','7'])
	    print(selected)

	    if isPlaying < 1:
	    	
	   		if last_received > '200':
				startVideo = startVideo + 1
				
				print(startVideo)
		
            			if startVideo > 0:				
							command = 'omxplayer -r -o local /home/pi/Desktop/Sensor/darth'+selected+'.mp3'
 							isPlaying = 1	    					
	   						child = pexpect.spawn(command)
          						time.sleep(3)
 	   						isPlaying = 0

receiving(ser)
 
# #start on runlevel [2345]
# #stop on runlevel [016]
# chdir /home/pi/Desktop/Sensor
# exec python /home/pi/Desktop/Sensor/Eileen1_POC.py
# respawn

