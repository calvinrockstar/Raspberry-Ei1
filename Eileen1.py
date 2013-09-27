import subprocess
import time
from serial import Serial
from subprocess import PIPE, STDOUT

ser = Serial('/dev/ttyACM0', 9600, timeout=1)
isPlaying = 0


def receiving(ser):
    global last_received
    global startVideo
	
    startVideo = 0
    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
	
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]
	    print(last_received)
	    	  
	    if last_received > '20' and last_received < '50':
			startVideo = startVideo + 1
			print(startVideo)
		
            		if startVideo > 5:	
	    				isPlaying = 1
					subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer1.sh", shell=True)
					#ser.close()
					time.sleep(10)
 					subprocess.call("pkill screen", shell=True)					
					print("Start video")

receiving(ser)
