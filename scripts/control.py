#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
from geometry_msgs.msg import Twist

def main():
	rospy.init_node("control", anonymous=True)
	pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

	while not rospy.is_shutdown():
		vel = Twist()
		direction = raw_input("f: forward, r: right, l: left > ")
		
		if direction == 'f':
			rospy.loginfo("Go ahead")
			vel.linear.x = 1.0 
		if direction == 'r':
			rospy.loginfo("Turn right")
			vel.angular.z = -math.pi/2
		if direction == 'l':
			rospy.loginfo("Turn left")
			vel.angular.z = math.pi/2
		if direction == 'q':
			break
		pub.publish(vel)

if __name__ == "__main__":
	main()
