#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
from math import pow, atan2, sqrt

class Turtlesim_goto_goal:
	def __init__(self):
			
		rospy.init_node('turtle_guide_to_xy')
		self.vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

		self.pose = Pose()
		self.rate = rospy.Rate(10)

	def update_pose(self, data):
		self.pose = data
		self.pose.x = round(self.pose.x, 4)
		self.pose.y = round(self.pose.y, 4)

	def euclidean_distance(self, goal_pose):
		return sqrt(pow((goal_pose.x - self.pose.x), 2) +
			    pow((goal_pose.y - self.pose.y), 2))

	def linear_vel(self, goal_pose, const=1.5):
		return const * self.euclidean_distance(goal_pose)

	def steering_angle(self, goal_pose):
		return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

	def angular_vel(self, goal_pose, const=5):
		return const * (self.steering_angle(goal_pose) - self.pose.theta)

	def move2goal(self):
		goal_pose = Pose()
		# get the input from the user
		goal_pose.x = float(input("Set your x goal: "))
		goal_pose.y = float(input("Set your y goal: "))

		# set your tolarence (0.01)
		distance_tolarence = float(input("Set your tolerance: "))

		vel_msg = Twist()

		while self.euclidean_distance(goal_pose) >= distance_tolarence:
			vel_msg.linear.x = self.linear_vel(goal_pose)
			vel_msg.angular.z = self.angular_vel(goal_pose)

			self.vel_publisher.publish(vel_msg)
			self.rate.sleep()

		vel_msg.linear.x = 0
		vel_msg.angular.z = 0 
		self.vel_publisher.publish(vel_msg)

		rospy.spin()

if __name__ == '__main__':
	try:
	     x = Turtlesim_goto_goal()
	     x.move2goal()
	except rospy.ROSInterruptException:
	     pass
