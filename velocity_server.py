#!/usr/bin/env python3

#Project-1
#WPI-RBE-500
#Date:-19-NOv-2021
#This program will take end effector pose as input and output the joint angles

from scara_control.srv import inv_jacobian, inv_jacobianResponse, jacobian, jacobianResponse
from sensor_msgs.msg import JointState
import rospy
import math

p1 = 0
p2 = 0
p3 = 0

def jacobian_callback_server(data):
	global p1
	global p2
	global p3
	q1 = data.q1
	q2 = data.q2
	q3 = data.q3

	vx = ((-math.sin(p1+p2) - math.sin(p1))*q1) + (-math.sin(p1+p2)*q2) 
	vy = ((math.cos(p1+p2) + math.cos(p1))*q1)+ (math.cos(p1+p2)*q2)
	vz = q3
	wx = 0
	wy = 0
	wz = q1+q2
	return jacobianResponse(vx,vy,vz,wx,wy,wz)

def invJacobian_callback_server(data_inv):
	vx = data_inv.vx
	vy = data_inv.vy
	vz = data_inv.vx
	wx = data_inv.wx
	wy = data_inv.wy
	wz = data_inv.wz

	q1 = 0
	q2 = 0
	q3 = 0
	return inv_jacobianResponse(q1,q2,q3)

def position_callback(pos):
	global p1
	global p2
	global p3
	p1 = pos.position[0]
	p2 = pos.position[1]
	p3 = pos.position[2]

def main_function():

	#creating node - inver_service_server for ros communication
	rospy.init_node("velocity_service_server")

	#Starting the service server 'jacobian' 
	rospy.Service('jacobian_server',jacobian,jacobian_callback_server)
	
	#Starting the service server 'inv_jacobian' 
	rospy.Service('invjacobian_server',inv_jacobian,invJacobian_callback_server)
	
	rospy.Subscriber("/scara/joint_states",JointState , position_callback)

	#make server run continously in a loop
	rospy.spin()

if __name__ == "__main__":
	main_function()