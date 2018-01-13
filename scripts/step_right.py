#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import math

CHANNEL1 = 31   #A_PHASE
CHANNEL2 = 33   #A_ENBLE
CHANNEL3 = 35   #B_PHASE
CHANNEL4 = 37   #B_ENBLE

WHEEL_SIZE =48 

def init():
	channels = [CHANNEL1,CHANNEL2,CHANNEL3,CHANNEL4]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(channels, GPIO.OUT, initial=GPIO.HIGH)

def clean_up():
	channels = [CHANNEL1,CHANNEL2,CHANNEL3,CHANNEL4]
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(channels, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.cleanup(channels)

def forward_rolling(rpm):
	pulse_time = 60.0 / rpm / 200.0
	#print "1"
	GPIO.output(CHANNEL1, 0)
	GPIO.output(CHANNEL2, 1)
	GPIO.output(CHANNEL3, 1)
	GPIO.output(CHANNEL4, 0)
	time.sleep(pulse_time)
	#print "2"
	GPIO.output(CHANNEL1, 0)
	GPIO.output(CHANNEL2, 1)
	GPIO.output(CHANNEL3, 0)
	GPIO.output(CHANNEL4, 1)
	time.sleep(pulse_time)
        #print "3"
	GPIO.output(CHANNEL1, 1)
	GPIO.output(CHANNEL2, 0)
	GPIO.output(CHANNEL3, 0)
	GPIO.output(CHANNEL4, 1)
	time.sleep(pulse_time)
	#print "4"
	GPIO.output(CHANNEL1, 1)
	GPIO.output(CHANNEL2, 0)
	GPIO.output(CHANNEL3, 1)
	GPIO.output(CHANNEL4, 0)
	time.sleep(pulse_time)


def inverted_rolling(rpm):
	pulse_time = 60.0 / rpm / 200.0
	#print "1"
	GPIO.output(CHANNEL1, 1)
	GPIO.output(CHANNEL2, 0)
	GPIO.output(CHANNEL3, 1)
	GPIO.output(CHANNEL4, 0)
	time.sleep(pulse_time)
        #print "2"
	GPIO.output(CHANNEL1, 1)
	GPIO.output(CHANNEL2, 0)
	GPIO.output(CHANNEL3, 0)
	GPIO.output(CHANNEL4, 1)
	time.sleep(pulse_time)
	#print "3"
	GPIO.output(CHANNEL1, 0)
	GPIO.output(CHANNEL2, 1)
	GPIO.output(CHANNEL3, 0)
	GPIO.output(CHANNEL4, 1)
	time.sleep(pulse_time)
	#print "4"
	GPIO.output(CHANNEL1, 0)
	GPIO.output(CHANNEL2, 1)
	GPIO.output(CHANNEL3, 1)
	GPIO.output(CHANNEL4, 0)
	time.sleep(pulse_time)


def main_loop(velocity):
	rpm = 60*float(velocity)/(math.pi*WHEEL_SIZE/1000)	
	init()	
	try:
		while True:	
			if rpm > 0:
				forward_rolling(rpm)
			else:
				inverted_rolling(-rpm)
	except KeyboardInterrupt:
		clean_up()

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 2:
		main_loop(args[1])
