import subprocess
import time
import pexpect

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
	    	  
	    if last_received > '50' and last_received < '80':
			startVideo = startVideo + 1
			print(startVideo)
		
            		if startVideo > 2:	
	    				isPlaying = 1
					command = 'omxplayer -r -o local /home/pi/Desktop/Sensor/vid1.mov'
					child = pexpect.spawn(command)

					#subprocess.call(['omxplayer','/home/pi/Desktop/Sensor/vid1.mov'])
					#pexpect.run('p')
					#child = pexpect.spawn (['omxplayer','/home/pi/Desktop/Sensor/vid1.mov'])
					child.expect('p')
					child.sendline('p')	
					
					#subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer1.sh", shell=True)
					#time.sleep(16)	
					#startVideo = 0	
					#subprocess.call("pkill screen", shell=True)			
					#print("Start video")

receiving(ser)