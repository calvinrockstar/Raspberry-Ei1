import time, subprocess

def PlayList(Movies):
	for movie in Movies:
		p = subprocess.Popen(["omxplayer", movie[0]])
		time.sleep(movie[1])
	PlayList(Movies)

#Movies list here name and length
Movies = [['vid1.mov',5],['vid2.mov',5]]
#Movies = [['vid3.mp4',5]]
PlayList(Movies)
