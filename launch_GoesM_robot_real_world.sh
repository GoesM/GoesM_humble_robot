#!/bin/bash
export ROS_LOG_DIR="ros_log"
export ASAN_OPTIONS=halt_on_error=0:new_delete_type_mismatch=0:detect_leaks=0:log_path=asan:detect_odr_violation=0
source install/setup.bash
ros2 launch my_bringup real_robot_nav2_slam_launch.py
