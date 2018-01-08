#!/usr/bin/env python

import rospy
import math
#import RPi.GPIO as GPIO
from std_msgs.msg import String
from geometry_msgs.msg import Twist

import subprocess

CHANNEL1 = 7   #A_PHASE
CHANNEL2 = 11   #A_ENBLE
CHANNEL3 = 13   #B_PHASE
CHANNEL4 = 15   #B_ENBLE

CHANNEL5 = 31   #A_PHASE
CHANNEL6 = 33   #A_ENBLE
CHANNEL7 = 35   #B_PHASE
CHANNEL8 = 37   #B_ENBLE

cmd = "python step.py"

def clean_up():
    channels = [CHANNEL1,CHANNEL2,CHANNEL3,CHANNEL4,CHANNEL5,CHANNEL6,CHANNEL7,CHANNEL8]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(channels, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.cleanup(channels)

def callback(data):
	print data
	
	if data.linear.x > 0:
		text = 'a',int(100 * data.linear.x)
	if data.linear.x == 0 and data.angular.z < 0:
		text = 'r',int(math.degrees(-data.angular.z))
	if data.linear.x == 0 and data.angular.z > 0:
		text = 'l',int(math.degrees(data.angular.z))
	
	#print text[0]
	#print text[1]
	'''
	if len(text) > 1:
		temp_cmd = cmd + " " + text[0] + " " + text[1]
		print temp_cmd
		proc = subprocess.Popen( temp_cmd .strip().split(" ") )
	
	if text[0] == 'c':
		proc.terminate()
		clean_up()
	'''
def main():	
	rospy.init_node("move_main", anonymous=True)
	rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
	rospy.spin()

if __name__ == "__main__":
	main()
