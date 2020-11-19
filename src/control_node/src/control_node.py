#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import socket

# Util imports
import random
import math
import time

ip = '169.254.254.169'
port = 80
ranges = []

def laser_callback(msg):
    global ranges
    ranges = msg.ranges

def movement():
    sub = rospy.Subscriber('/scan', LaserScan, laser_callback)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist ,queue_size=1)
    rospy.init_node('control_node')
    rate = rospy.Rate(10)
    cmd=Twist()
    while not rospy.is_shutdown():
        global ranges
        front=ranges[180]
        l_front=ranges[225]
        r_front=ranges[135]
        right=ranges[90]
        left=ranges[270]
        l_back=ranges[315]
        r_back=ranges[45]
        thres=0.5
        s_thres=0.35
        if l_front<thres and r_front<thres:
            cmd.linear.x = 0.5
            cmd.angular.z = 0.0
            pub.publish(cmd)
            print (0.5,0.0)
            rate = rospy.Rate(1)
            rate.sleep()
        # elif l_front>thres and r_front>thres and left<s_thres and right<s_thres:
        # elif l_front>thres and r_front>thres and l_back<thres and r_back<thres:    
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = 0
            pub.publish(cmd)
            print (0.0,0)
            rate = rospy.Rate(10)
            rate.sleep()

        # cmd2send="%03.2f*%03.2f" %(cmd.linear.x, cmd.angular.z) 
        # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client.connect((socket.gethostname(), port))
        # client.send(("GET /cmd?=C01" + cmd2send).encode('utf-8'))
        # client.close()    
    # Create a Twist message and add linear x and angular z values


if __name__ == '__main__':
    try:
        movement()
    except rospy.ROSInterruptException:
        pass



rospy.spin()
