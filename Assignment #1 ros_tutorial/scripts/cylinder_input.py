#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node("cylinder_input")
radius_pub = rospy.Publisher("/radius", Float64, queue_size=10)
height_pub = rospy.Publisher("/height", Float64, queue_size=10)
rho_pub = rospy.Publisher("/rho", Float64, queue_size=10)


radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
rho = float(input("Enter rho: "))

while not rospy.is_shutdown():
	radius_pub.publish(radius)
	height_pub.publish(height)
	rho_pub.publish(rho)
	rospy.sleep(0.1)
	
	

