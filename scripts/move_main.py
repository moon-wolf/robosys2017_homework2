#!/usr/bin/env python

import rospy
import math
import time
import RPi.GPIO as GPIO
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

WIDTH = 90

CMD_R = "python step_right.py"
CMD_L = "python step_left.py"

def clean_up():
    channels = [CHANNEL1,CHANNEL2,CHANNEL3,CHANNEL4,CHANNEL5,CHANNEL6,CHANNEL7,CHANNEL8]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(channels, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.cleanup(channels)

def callback(data):
	velocity_r = 0
	velocity_l = 0

	rospy.loginfo("data.linear.x  :%s [m/s]",data.linear.x)
	rospy.loginfo("data.angular.z :%s [rad/s]",data.angular.z)

	if data.angular.z != 0:
		velocity_r = float(WIDTH)*math.pi*data.angular.z/(4*1000)
		velocity_l = -float(WIDTH)*math.pi*data.angular.z/(4*1000)

	if data.linear.x > 0:
		velocity_r += data.linear.x
		velocity_l += data.linear.x

	temp_r = CMD_R + ' ' + str(velocity_r)
	temp_l = CMD_L + ' ' + str(velocity_l)
	r_proc = subprocess.Popen(temp_r.strip().split(" "))
	l_proc = subprocess.Popen(temp_l.strip().split(" "))
	time.sleep(1)
	r_proc.terminate()
	l_proc.terminate()
	clean_up()
	
def main():	
	rospy.init_node("move_main", anonymous=True)
	rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
	rospy.spin()

if __name__ == "__main__":
	main()
