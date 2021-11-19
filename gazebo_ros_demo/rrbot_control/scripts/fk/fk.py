#!/usr/bin/env python3
import rospy

from sensor_msgs.msg import JointState
import numpy as np
from tf.transformations import euler_from_matrix


def callback_joints(joint_data):
	# print(joint_data.position[0])

	print('------------------------------------------------------------------------------')

	j1 = joint_data.position[0]
	j2 = joint_data.position[1]
	j3 = joint_data.position[2]

	#link lengths
	l1 = a1 = 1
	l2 = a2 = 1
	l3 = a3 = 0.5
	

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

	alpha, beta, gamma = euler_from_matrix(t[0:3, 0:3], 'rzyz')

	alpha = round(alpha*180/np.pi, 2)
	beta = round(beta*180/np.pi, 2)
	gamma = round(gamma*180/np.pi, 2)

	print('position',t[0:3, 3])
	#print('alpha,beta,gamma',alpha,beta,gamma)


	
def listener():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber("/joint_states", JointState, callback_joints)

	# spin() simply keeps python from exiting until this node is stopped
	rate = rospy.Rate(100)
	rate.sleep()
	rospy.spin()
	# rate = rospy.Rate(10)

if __name__ == '__main__':
	listener()