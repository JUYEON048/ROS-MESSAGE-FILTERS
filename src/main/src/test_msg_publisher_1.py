#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from test_msg.msg import *

class test_msg_pubs_1(object):
    def __init__(self):
        self.t1_msg = TEST()
        self.t1_pub = rospy.Publisher('t1', TEST, queue_size = 10)
        

    def t1_publisher(self, event):
        self.t1_msg.header.stamp = rospy.Time.now()
        self.t1_msg.header.frame_id = "t1"
        self.t1_msg.data = 1.0        
        return self.t1_pub.publish(self.t1_msg)
    

if __name__ == '__main__':
    rospy.init_node('TestMsgPub1', anonymous=True)
    TMP1 = test_msg_pubs_1()
    timer = rospy.Timer(rospy.Duration(0.2), TMP1.t1_publisher)
    rospy.spin()
