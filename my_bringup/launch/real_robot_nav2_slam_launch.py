import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    return LaunchDescription([
        # 输出信息
        LogInfo(
            condition=None,
            msg="Launching my_bringup..."),

        # 启动slam_toolbox的launch文件
        IncludeLaunchDescription(
            launch_description_path=os.path.join(
                get_package_share_directory('slam_toolbox'),
                'launch', 'online_sync_launch.py'),
            launch_arguments={}.items()),

        # 启动nav2_bringup的rviz_launch文件
        IncludeLaunchDescription(
            launch_description_path=os.path.join(
                get_package_share_directory('nav2_bringup'),
                'launch', 'rviz_launch.py'),
            launch_arguments={}.items()),

        # 启动nav2_bringup的navigation_launch文件
        IncludeLaunchDescription(
            launch_description_path=os.path.join(
                get_package_share_directory('nav2_bringup'),
                'launch', 'navigation_launch.py'),
            launch_arguments={}.items())
    ])
