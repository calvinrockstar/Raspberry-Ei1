import subprocess
import time
import uinput

from serial import Serial
from subprocess import PIPE, STDOUT

ser = Serial('/dev/ttyACM0', 9600, timeout=1)
isPlaying = 0
device = uinput.Device([uinput.KEY_P])

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
					
					#subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer1.sh", shell=True)
					subprocess.call(['omxplayer','/home/pi/Desktop/Sensor/vid1.mov'])
					
					#subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer2.sh", shell=True)
					#subprocess.call("bash /home/pi/Desktop/Sensor/videoDie1.sh", shell=True)
					time.sleep(2)
					device.emit_click(uinput.KEY_P)
					
					
					
					#time.sleep(16)
					#psubprocess.call("screen -d vid2")
					#subprocess.call(['omxplayer','/home/pi/Desktop/Sensor/vid1.mov'])
					#ser.close()
					#subprocess.call("screen -X -S vid1 quit")
					#time.sleep(5)
					#subprocess.call(['omxplayer','/home/pi/Desktop/Sensor/vid1.mov'])
					#subprocess.call("screen -X -S vid1 quit", shell=True)
					#subprocess.call("bash /home/pi/Desktop/Sensor/videoplayer2.sh", shell=True)
					#time.sleep(20)
 					#subprocess.call("pkill screen", shell=True)
					#subprocess.call("killall omxplayer.bin", shell=True)
					#subprocess.call(['omxplayer','/home/pi/Desktop/Sensor/vid2.mov'])					
					print("Start video")

receiving(ser)

