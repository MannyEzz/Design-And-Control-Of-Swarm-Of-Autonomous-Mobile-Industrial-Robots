#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def callback():
    vel_msg = Twist()
    vx = vel_msg.linear.x
    vy = vel_msg.linear.y
    thetaz = vel_msg.angular.z

    w1 = ( (vx-vy-(0.17+0.19)*thetaz)/0.08) 
    w2 = ( (vx+vy+(0.17+0.19)*thetaz)/0.08)    
    w3 = ( (vx+vy-(0.17+0.19)*thetaz)/0.08)  
    w4 = ( (vx-vy+(0.17+0.19)*thetaz)/0.08)

    rospy.loginfo(%w1)
    rospy.loginfo(%w2)    
    rospy.loginfo(%w3)    
    rospy.loginfo(%w4)    
    

    
if __name__ == '__main__':
   try:
    rospy.init_node('urdf_final', anonymous=True) 
    rospy.Subscriber('/cmd_vel', Twist,callback)
    rospy.spin()
   except rospy.ROSInterruptException: pass
