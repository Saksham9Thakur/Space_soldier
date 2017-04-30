import serial
import os,time
import RPi.GPIO as GPIO
import sys
#from app import app, db
GPIO.setmode(GPIO.BOARD)
ser = serial.Serial('/dev/ttyACM0',9600)
#print ser
#assert False
m=''
x=''
while True: 
	x = str(ser.readline())
	if(x==m):
	 	pass
	else:
	 	m=x
	 	c=db.sesssion.add(last(m))
	 	db.sesssion.commit(c)
