#!/usr/bin/env python3


# import Ros for writing the node
import rospy

#import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist


if __name__ == '__main__':
	# declare a publisher to publish turtle velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size = 10)
	# initilize the ROS node
	rospy.init_node('vel_publisher_node' , anonymous = True)
	# define a loop rate and set the frequency to 10 Hz
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist (just an empty message)
	vel_cmd = Twist()
	# run a control loop on a regular basis (every 0.1 seconds)
	while not rospy.is_shutdown():
		# set the linear velocity command
		vel_cmd.linear.x = 0.5
		#set the angular velocity command
		vel_cmd.angular.z = 0.5
		# publish the velocity command
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 second and go to next step
		loop_rate.sleep()
		
