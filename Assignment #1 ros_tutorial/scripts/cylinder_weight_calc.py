#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

from math import pi

radius_squared = 0
height = 0
rho = 0

radius_squared_found = False
height_found = False
rho_found = False

def radius_squared_callback(data):
	global radius_squared
	global radius_squared_found
	radius_squared = data.data
	radius_squared_found = True	

def height_callback(data):
	global height
	global height_found
	height = data.data
	height_found = True

def rho_callback(data):
	global rho
	global rho_found
	rho = data.data
	rospy.logwarn("rho: %f", rho )
	rho_found = True

def calculate():
	if radius_squared_found and height_found and rho_found:
		msg = Cylinder()
		msg.cylinder_weight = pi * radius_squared * rho
		pub.publish(msg)
	
rospy.init_node("cylinder_weight_calc")
rospy.Subscriber("/rho", Float64, rho_callback)
rospy.Subscriber("/radius_squared", Float64, radius_squared_callback)
rospy.Subscriber("/height", Float64, height_callback)

pub =  rospy.Publisher("/cylinder_weight", Cylinder, queue_size=10)

while not rospy.is_shutdown():
	calculate()
	rospy.sleep(0.1)
	
	

