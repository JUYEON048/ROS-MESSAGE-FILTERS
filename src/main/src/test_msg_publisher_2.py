#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from test_msg.msg import *

class test_msg_pubs_2(object):
    def __init__(self):
        self.t2_msg = TEST()
        self.t2_pub = rospy.Publisher('t2', TEST, queue_size = 10)
        
        
    def t2_publisher(self, event):
        self.t2_msg.header.stamp = rospy.Time.now()
        self.t2_msg.header.frame_id = "t2"
        self.t2_msg.data = 1.0        
        return self.t2_pub.publish(self.t2_msg)
    
    

if __name__ == '__main__':
    rospy.init_node('TestMsgPub2',anonymous=True)
    TMP2 = test_msg_pubs_2()
    timer = rospy.Timer(rospy.Duration(0.01), TMP2.t2_publisher)
    rospy.spin()
