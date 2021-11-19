#!/usr/bin/env python3

from rrbot_control.srv import inv_kin, inv_kinResponse
import rospy
import math

def callback_server(data_inv):
	
	x = data_inv.x
	y = data_inv.y
	z = data_inv.z

	r 	= data_inv.r
	p 	= data_inv.p
	r_y = data_inv.r_y

	print(x)
	print(y)
	print(z)
	h = math.sqrt(x*x + y*y)

	k = (h*h - 2)/2

	th_2 = math.atan2(math.sqrt(1-k*k),k)
	th_3 = z - 1.2
	th_1 = math.atan2(y,x) - math.atan2(math.sin(th_2), 1+math.cos(th_2))

	print(round(th_1,2))
	print(round(th_2,2))
	print(round(th_3,2))

	return inv_kinResponse(round(th_1,2),round(th_2,2),round(th_3,2))

def main_function():

	rospy.init_node("inver_service_server")
	rospy.Service('inver_server',inv_kin,callback_server)
	rospy.spin()

if __name__ == "__main__":
	main_function()