#/bin/bash

screen -dmS vid2 sh -c 'omxplayer -r -o local /home/pi/Desktop/Sensor/vid2.mov; exec bash'
