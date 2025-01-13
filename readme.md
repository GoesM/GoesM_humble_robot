# GoesM-Humble-Robot
基于ROS2-humble各版本项目，和本人对这些仓库使用的个人习惯，创建本仓库

目的是，便利我自己未来可能需要的工程部署

### 主要涵盖以下内容
- 编译脚本 [插桩编译脚本asan_colcon](asan_colcon.py), [普通编译脚本common_colcon](common_colcon.py) 
- 启动脚本 [launch**](launch_nav2_bringup.sh)
- 便捷使用脚本 [quick_use](quick_use/)

### 包含ROS2项目
- navigation2: 自主导航系统
```sh
git clone https://github.com/ros-navigation/navigation2 -b humble
```
- slam_toolbox： 雷达建图系统 
```sh
git clone https://github.com/SteveMacenski/slam_toolbox -b humble
```