#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import message_filters
from test_msg.msg import *  # in sync.msg


def m_filters_callback(t1_msg, t2_msg):
    #print("mfilters_callback ::", t1_msg.header, t2_msg.header)
    print("mfilters_callback ::", t1_msg.data, t2_msg.data)


if __name__ == '__main__':

    rospy.init_node('message_filter',anonymous=True)
    
    t1_sub = message_filters.Subscriber("/t1", TEST)
    t2_sub = message_filters.Subscriber("/t2", TEST)

    #message_filters.ApproximateTimeSynchronizer([subsciber], Queue size ,Time interval, allow headerless Flag(True or False))
    m_filters = message_filters.ApproximateTimeSynchronizer([t1_sub, t2_sub], 10 , 0.1, allow_headerless=False)
    
    m_filters.registerCallback(m_filters_callback)
    rospy.spin()










