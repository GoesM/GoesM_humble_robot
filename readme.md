# GoesM-Humble-Robot
基于ROS2-humble各版本项目，和本人对这些仓库使用的个人习惯，创建本仓库

目的是，便利我自己未来可能需要的工程部署

## 仓库代码结构介绍
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


## GoesM Robot 使用流程
### 通过Gazebo仿真使用nav2（支持未知地图探索）
- step 1. `./launch_gazebo.sh`
- step 2. `./launch_rviz.sh`
- step 3. `./launch_nav2.sh`
- step 4. `./launch_async_slam.sh`

### 在real robot上使用nav2（支持未知地图探索）
- step 1. 启动real robot中 与底盘通信的ROS2节点。
- step 2. `./launch_rviz.sh`
- step 3. `./launch_nav2.sh`
- step 4. `./launch_async_slam.sh`


### TODO
- [ ] 将上述步骤封装为my_bringup
- [ ] my_bringup对上述项目集成启动后，会发生很多很奇怪的错误，需要调试。
- [ ] [launch_GoesM_robot_real_world.sh](launch_GoesM_robot_real_world.sh)
- [ ] [launch_GoesM_robot_simulator.sh](launch_GoesM_robot_simulator.sh)