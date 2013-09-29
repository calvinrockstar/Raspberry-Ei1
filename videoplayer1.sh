#/bin/bash

screen -dmS vid1 sh -c 'omxplayer -r -o local /home/pi/Desktop/Sensor/vid1.mov; exec bash'

#screen -dmS vid2 sh -c 'omxplayer -r -o local --win "960 0 1920 540" /home/pi/Desktop/Sensor/vid2.mov; exec bash'

#screen -dmS vid1 sh -c 'omxplayer -r -o local /home/pi/Desktop/Sensor/vid1.mov; exec bash'

#screen -dmS vid1 sh -c 'omxplayer -r -o local "200 100 1240 800" /home/pi/Desktop/Sensor/vid1.mov; exec bash'
#screen -dmS vid2 sh -c 'omxplayer -r --win "200 0 720 288" /home/pi/Desktop/Sensor/vid2.mov; exec bash'
