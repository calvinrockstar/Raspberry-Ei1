import pexpect

from pyomxplayer import OMXPlayer
from pprint import pprint
omx = OMXPlayer('/home/pi/Desktop/Sensor/vid1.mov')
pprint(omx.__dict__)

