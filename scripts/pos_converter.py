#!/usr/bin/env python3

import rospy
# read turtlesim/Pose message
from turtlesim.msg import Pose
# import math module to convert radians to degree
import math

# declare constant for the angular position scales
ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):
	# convert angular positions
	rot_in_degrees = data.theta * ROTATION_SCALE
	# convert x and y to cm
	x_in_cm = data.x * 100
	y_in_cm = data.y * 100
	# show the results on screen
	rospy.loginfo("x is %0.2f cm,  y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degrees)


if __name__ == '__main__':
	# intialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add subscriber to read pos info from turtle1/pos
	rospy.Subscriber('/turtle1/pos', Pose, pose_callback)
	# spin() keeps python from exiting until node is stopped
	rospy.spin()
