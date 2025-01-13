from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from launch.substitutions import ThisLaunchFileDir
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')
    slam_toolbox_launch_dir = os.path.join(slam_toolbox_dir, 'launch')

    nav2_dir = get_package_share_directory('nav2_bringup')
    nav2_launch_dir = os.path.join(nav2_dir, 'launch')

    gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    gazebo_launch_dir = os.path.join(gazebo_dir, 'launch')
    
    return LaunchDescription([
        # 启动 nav2_bringup rviz_launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, 'rviz_launch.py')
            ),
        ),
        # 启动 nav2_bringup navigation_launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, 'navigation_launch.py')
            ),
        ),
        # 启动 turtlebot3_gazebo turtlebot3_world.launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_launch_dir, 'turtlebot3_world.launch.py')
            ),
        ),
    ])
