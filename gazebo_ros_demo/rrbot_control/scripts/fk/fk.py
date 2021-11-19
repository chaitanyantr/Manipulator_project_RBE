#!/usr/bin/env python3

#Project-1
#This program will take joint angles as input and output the end effector pose of scara-3dof arm
#WPI-RBE-500
#Date:-19-Nov-2021

import rospy
from sensor_msgs.msg import JointState
from tf.transformations import euler_from_matrix
import numpy as np
from geometry_msgs.msg import Twist


def callback_joints(joint_data):
	# print(joint_data.position[0])

	print('------------------------------------------------------------------------------')

	# Getting the joint angles from joint_states topic 
	#joint_data is an array of angles and also parametric varible for the data accessing

	j1 = joint_data.position[0]
	j2 = joint_data.position[1]
	j3 = joint_data.position[2]

	#link lengths of arm - l1-revolute-link1,l2-revolute-link2,l3-prismatic-link
	l1 = a1 = 1
	l2 = a2 = 1
	l3 = a3 = 0.5

	# H-Matrix for scara robot arm - 3dof
	r11 = np.cos(j1)*np.cos(j2) - np.sin(j1)*np.sin(j2)
	r12 = np.cos(j1)*np.sin(j2) - np.cos(j2)*np.sin(j1)
	r13 = 0
	r14 = a1*np.cos(j1) + a2*np.cos(j1+j2)

	r21 = np.cos(j1)*np.sin(j2) + np.cos(j2)*np.sin(j1)
	r22 = np.sin(j1)*np.sin(j2) - np.cos(j1)*np.cos(j2)
	r23 = 0
	r24 = a1*np.sin(j1) + a2*np.sin(j1+j2)

	r31 = 0
	r32 = 0
	r33 = 1
	r34 = 2+a3

	r41 = 0
	r42 = 0
	r43 = 0
	r44 = 1

	t = np.matrix([[r11,r12,r13,r14],[r21,r22,r23,r24],[r31,r32,r33,r34],[r41,r42,r43,r44]])

	#Getting angles from 3d-Rotation matrix and converting to euler form

	alpha, beta, gamma = euler_from_matrix(t[0:3, 0:3], 'rzyz')

	alpha = round(alpha*180/np.pi, 2)
	beta = round(beta*180/np.pi, 2)
	gamma = round(gamma*180/np.pi, 2)

	#print('position',t[0:3, 3])
	#print('alpha,beta,gamma',alpha,beta,gamma)


	pub_pose = rospy.Publisher('arm_pose',Twist,queue_size=10)

	arm_pose = Twist()

	arm_pose.linear.x = t[0,3]
	arm_pose.linear.y = t[1,3]
	arm_pose.linear.z = t[2,3]

	arm_pose.angular.x = alpha
	arm_pose.angular.y = beta
	arm_pose.angular.z = gamma
	
	pub_pose.publish(arm_pose)

	
def listener():

	#creating ros node
	rospy.init_node('listener', anonymous=True)

	#subscribing topic for joint angles 
	rospy.Subscriber("/joint_states", JointState, callback_joints)

	# spin() simply keeps python from exiting until this node is stopped
	pub_pose = rospy.Publisher('arm_pose',Twist,queue_size=10)

	rate = rospy.Rate(100)
	rate.sleep()

	rospy.spin()
	
if __name__ == '__main__':
	listener()