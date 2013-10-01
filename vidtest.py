import time, subprocess
import Eileen1_POC

def PlayList(Movies):
	for movie in Movies:
		p = subprocess.Popen(["omxplayer", movie[0]])
		time.sleep(movie[1])
		PlayList(Movies)

#Movies list here name and length
Movies = [['vid1.mov',15],['vid2.mov',15],['vid1.mov',15]]
PlayList(Movies)
