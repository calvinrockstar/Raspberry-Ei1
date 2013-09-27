#!/usr/bin/python3

import subprocess
from serial import Serial
from subprocess import PIPE, STDOUT

ser = Serial('/dev/ttyACM0', 9600, timeout=1)
isPlaying = 0
print("connected to: " + ser.portstr)

#player = subprocess.Popen(['omxplayer','/home/pi/Desktop/Hammer2.mp3'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#player = subprocess.Popen(['omxplayer','/home/pi/Desktop/vid1.mov'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    # Read a line and convert it from b'xxx\r\n' to xxx
    line = ser.readline().decode('utf-8')[:-2]
    vol = 100
    if line:  # If it isn't a blank line
        print(line)
        if line < '20':
			if isPlaying == 0:
				subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer1.sh", shell=True)
				isPlaying == 1 
			#else:
				
	    	#if vol == 100:
            		#player.stdin.write('-') 
			#subprocess.call(['omxplayer','/home/pi/Desktop/vid1.mov'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		
            	#else:
	    		#vol= vol - 10
	
	    #player.wait()	    
	#subprocess.call(['omxplayer','/home/pi/Desktop/vid1.mov','shell=True'])
        elif line > '100':
		if vol < 100:
            		#subprocess.Popen(['omxplayer','/home/pi/Desktop/vid1.mov'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			#player.stdin.write('+')
			vol= vol+10
       
            #subprocess.call(['omxplayer','/home/pi/Desktop/Hammer2.mp3','shell=True'])
            #subprocess.call(["omxplayer", "p"])
        elif line == '110':
            break

ser.close()