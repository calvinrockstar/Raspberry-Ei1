import serial
>>> ser = serial.Serial('/dev/ttyACM0',9600)
>>> value = ser.readline()
while 1 :
	print(value)

