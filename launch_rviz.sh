#!/bin/bash
export ROS_LOG_DIR="ros_log"
source install/setup.bash
ros2 launch nav2_bringup rviz_launch.py