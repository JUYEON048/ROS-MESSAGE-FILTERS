cmake_minimum_required(VERSION 3.0.2)
project(main)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
    std_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

