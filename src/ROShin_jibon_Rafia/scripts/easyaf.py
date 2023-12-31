#!/usr/bin/env python 
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
rospy.init_node('first_node', anonymous=True)
pub=rospy.Publisher('chatter',String,queue_size=10)
rate =rospy.Rate(10)

while not rospy.is_shutdown():
str = "Bye Bye Workshop"
rospy.loginfo(str)
rate.sleep()
